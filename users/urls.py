from django.urls import path
from users.views import register, active_user, user_profile, profile_edit, CustomLogin, CustomPassResetView, CustomPassResetConfirmView
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('profile/', user_profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<int:user_id>/<str:token>/', active_user),
    path('change_password/', PasswordChangeView.as_view(template_name = 'registration/pass_change_form.html'), name='change_password'),
    path('pass_change_done/', PasswordChangeDoneView.as_view(template_name = 'registration/pass_change_done.html'), name='password_change_done'),
    path('pass_reset/', CustomPassResetView.as_view(), name='pass_reset'),
    path('pass_reset_confirm/<uidb64>/<token>/', CustomPassResetConfirmView.as_view(), name='password_reset_confirm')
]
