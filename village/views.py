from django.shortcuts import render, redirect
from django.http import HttpResponse
from village.models import Complain, Village
from village.forms import ComplainForm, VillageForm, ResponseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


User = get_user_model()

@login_required
def admin_dashboard(request):
    staff_users = User.objects.filter(is_staff=True)
    normal_users = User.objects.filter(is_staff=False)
    return render(request, 'dashboard/admin_dash.html', {'staff_users':staff_users, 'normal_users':normal_users})

@login_required
def dashboard(request):
    status = request.GET.get('status')
    specific_user = request.GET.get('my')

    status_count = Complain.objects.aggregate(
        total = Count('id'),
        pending = Count('id', filter=Q(status='pending')),
        resolved = Count('id', filter=Q(status='resolved')),
        rejected = Count('id', filter=Q(status='rejected'))
    )
    if status in ['pending', 'resolved', 'rejected']:
        complains = Complain.objects.filter(status=status).select_related('user').prefetch_related('tags')
    elif specific_user == 'true':
        complains = Complain.objects.select_related('user').prefetch_related('tags').filter(user_id=request.user.id)
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

"""Function based view
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
"""

class ComplainCreateView(LoginRequiredMixin, CreateView):
    form_class = ComplainForm
    template_name = 'complain/complain.html'
    success_url = reverse_lazy('complain')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Your complain created successfully !")
        return super().form_valid(form)
    

""" Function Based View 
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
"""

class UpdateComplain(LoginRequiredMixin, UpdateView):
    model = Complain
    form_class = ComplainForm
    template_name = 'complain/complain.html'
    pk_url_kwarg = 'user_id'

    def form_valid(self, form):
        messages.success(self.request, "Your complain updated successfully !")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating your complain !")
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('update_complain', kwargs={'user_id':self.object.id})
    
        
@login_required
def delete_complain(request, complain_id):
    complain = Complain.objects.select_related('user').prefetch_related('tags').get(id=complain_id)
    if request.method == 'POST':
        complain.delete()
        messages.success(request, "This complain deleted successfully !")
        return redirect('dashboard')
    return render(request, 'dashboard/dashboard.html', {'complain':complain})

@login_required
def complain_detail(request, user_id):
    complain = Complain.objects.select_related('user').prefetch_related('tags').get(id=user_id)
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
        form = VillageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your village created successfull!")
            return redirect('create_village')
    return render(request, "village/create_village.html", {'form':form})

@login_required
def update_village(request, village_id):
    village = Village.objects.get(id=village_id)
    form = VillageForm(instance=village)
    if request.method == 'POST':
        form = VillageForm(request.POST, request.FILES, instance=village)
        if form.is_valid():
            form.save()
            messages.success(request, "Village updated successfully !")
            return redirect('update_village', village_id)
    return render(request, 'village/create_village.html', {'form':form})

@login_required
def delete_village(request, village_id):
    village = Village.objects.get(id=village_id)
    if request.method == 'POST':
        village.delete()
        messages.success(request, "Village deleted succesfull !")
        return redirect('dashboard')
    return render(request, 'dashboard/dashboard.html', {'village':village})

@login_required
def village_information(request):
    villages = Village.objects.all()
    return render(request, 'village/village_information.html', {'villages': villages})

@login_required
def give_response(request, complain_id):
    complain = Complain.objects.select_related('user').prefetch_related('tags').get(id=complain_id)
    form = ResponseForm()
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.complain = complain
            response.responder = request.user
            response.save()
            messages.success(request, "Response submitted succesfull !")
            return redirect('complain_detail', user_id = complain.id)
    return render(request, 'response/response_form.html', {"form":form, "complain":complain})

@login_required
def assign_staff(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.success(request, f"{user.first_name} is now staff member !")
    return redirect('admin_dashboard')

@login_required
def remove_staff(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = False
    user.save()
    messages.success(request, f"{user.first_name} is now normal user !")
    return redirect('admin_dashboard')

@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.success(request, f"{user.first_name} is deleted successfully !")
    return redirect('admin_dashboard')
