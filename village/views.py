from django.shortcuts import render, redirect
from django.http import HttpResponse
from village.models import Complain, Tag
from village.forms import ComplainForm, VillageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q

@login_required
def dashboard(request):
    status = request.GET.get('status')
    status_count = Complain.objects.aggregate(
        total = Count('id'),
        pending = Count('id', filter=Q(status='pending')),
        resolved = Count('id', filter=Q(status='resolved')),
        rejected = Count('id', filter=Q(status='rejected'))
    )
    if status in ['pending', 'resolved', 'rejected']:
        complains = Complain.objects.filter(status=status).select_related('user').prefetch_related('tags')
    else:
        complains = Complain.objects.select_related('user').prefetch_related('tags').all()

    context = {
        'total_complains':status_count['total'],
        'pending':status_count['pending'],
        'resolved':status_count['resolved'],
        'rejected':status_count['rejected'],
        'complains':complains
    }
    return render(request, "dashboard/dashboard.html", context)

@login_required
def complain(request):
    form = ComplainForm()
    if request.method == 'POST':
        form = ComplainForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            form.save_m2m()
            messages.success(request, "Your complain created successfull!")
            return redirect('complain')
    return render(request, 'complain/complain.html', {'form':form})

@login_required
def update_complain(request, user_id):
    complain = Complain.objects.select_related('user').prefetch_related('tags').get(id=user_id)
    form = ComplainForm(instance=complain)

    if request.method == 'POST':
        form = ComplainForm(request.POST, request.FILES, instance=complain)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your complain update successfully!")
            return redirect('update_complain', user_id=complain.id)
    return render(request, 'complain/complain.html', {"form":form})

@login_required
def complain_detail(request, user_id):
    complain = Complain.objects.prefetch_related('tags').get(id=user_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['pending', 'resolved', 'rejected']:
            complain.status = new_status
            complain.save()
            messages.success(request, f"Status updated to {new_status} sucessfully !")
            return redirect('complain_detail', user_id=complain.id)
    return render(request, 'complain/complain_detail.html', {'complain': complain})



@login_required
def create_village(request):
    form = VillageForm()
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your village created successfull!")
            return redirect('create_village')
    return render(request, "village/create_village.html", {'form':form})


