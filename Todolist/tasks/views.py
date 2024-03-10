
from html import escape
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify


from tasks.models import Collection, Task

# Create your views here.
def index(request):
    context = {}

    collection_slug = request.GET.get("collection")
    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)

    context["collections"] = Collection.objects.order_by("slug")
    context["tasks"] = collection.task_set.all()

    return render(request, 'tasks/index.html', context=context)

def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))
    if not created:
        return HttpResponse("La collection existe déjà ", status=409)
    return HttpResponse(f'<h2>{collection_name}</h2>')


def add_task(request):
    collection = Collection.get_default_collection()
    description = escape(request.POST.get("task-description"))
    Task.objects.create(description=description, collection=collection)
    return HttpResponse(description)

def get_tasks(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    tasks = collection.task_set.all()
    return HttpResponse("<br>".join(task.description for task in tasks))
    
    