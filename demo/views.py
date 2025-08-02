from django.shortcuts import render
from django.http import HttpResponse
from demo.forms import DemoForm, Modelform
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
    if request.method == 'POST':
        form = DemoForm(request.POST, person=person)
        if form.is_valid():
            print(form.cleaned_data)

    return render(request, "use_form.html", {"form": form})

def model_form(request):
    form = Modelform()
    if request.method == 'POST':
        form = Modelform(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    return render(request, 'model_form.html', {"form":form})