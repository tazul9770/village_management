from django.shortcuts import render
from django.http import HttpResponse
from demo.forms import DemoForm
from demo.models import Person

def home(request):
    return HttpResponse("Django install successfull!")

def user(request):
    return render(request, "dashboard/user_dashboard.html")

def manager(request):
    return render(request, "dashboard/manager_dashboard.html")

def send_context(request):
    context = {
        "name" : "Tazul",
        "rate" : 32,
        "age" : 24
    }
    return render(request, "context.html", context)

def use_form(request):
    person = Person.objects.all()
    form = DemoForm(person=person)
    return render(request, "use_form.html", {"form": form})