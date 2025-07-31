from django.urls import path
from demo.views import home, user, manager, send_context

urlpatterns = [
    path('home/', home),
    path('user/', user),
    path('manager/', manager),
    path('context/', send_context)
]
