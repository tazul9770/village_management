from django.shortcuts import render, redirect
from django.http import HttpResponse
from village.forms import ComplainForm, VillageForm
from django.contrib import messages

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def complain(request):
    form = ComplainForm()
    if request.method == 'POST':
        form = ComplainForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            print(form.cleaned_data)
            messages.success(request, "Your complain created successfull!")
            return redirect('complain')
    return render(request, 'complain/complain.html', {'form':form})

def create_village(request):
    form = VillageForm()
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your village created successfull!")
            return redirect('create_village')
    return render(request, "village/create_village.html", {'form':form})


