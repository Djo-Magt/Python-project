from django.http import HttpResponse
from django.shortcuts import render
from website.forms import SignupForm
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"
    title = "default"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

# Create your views here.
def blog_post(request):
    return HttpResponse("BlogPost")

def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", context={"form": form})

