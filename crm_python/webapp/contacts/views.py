from django.shortcuts import redirect, render
from api.crm import User, get_all_users

def index(request):
    return render(request, 'contacts/index.html', {'users': get_all_users()})


def add_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    address = request.POST.get("address")
    phone_number = request.POST.get("phone_number")

    user = User(first_name, last_name, address, phone_number)
    user.save()

    return redirect('index')

def delete_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    user = User(first_name, last_name)
    user.delete()
    return redirect('index')
