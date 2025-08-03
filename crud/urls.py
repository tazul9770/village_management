from django.urls import path
from crud.views import show_data

urlpatterns = [
    path('show_data/', show_data)
]
