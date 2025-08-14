from django.urls import path
from users.views import register, log_in, log_out, active_user, user_profile, profile_edit, assign_role, create_group, show_group

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('profile/', user_profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('logout/', log_out, name='logout'),
    path('activate/<int:user_id>/<str:token>/', active_user),
    path('assign_role/<int:user_id>/', assign_role, name='assign_role'),
    path('create_group/', create_group, name='create_group'),
    path('show_group/', show_group, name='show_group')
]
