from django.urls import path
from demo.views import home, user, manager, send_context, use_form

urlpatterns = [
    path('home/', home),
    path('user/', user),
    path('manager/', manager),
    path('context/', send_context),
    path('use_form/', use_form)
]
