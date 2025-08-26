from django.urls import path
from users.views import register, log_in, log_out, active_user, user_profile, profile_edit, CustomLogin

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('profile/', user_profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('logout/', log_out, name='logout'),
    path('activate/<int:user_id>/<str:token>/', active_user)
]
