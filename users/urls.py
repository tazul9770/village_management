from django.urls import path
from users.views import register, log_in, log_out, active_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('activate/<int:user_id>/<str:token>/', active_user)
]
