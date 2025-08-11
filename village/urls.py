from django.urls import path
from village.views import test

urlpatterns = [
    path('test/', test)
]
