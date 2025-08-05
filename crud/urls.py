from django.urls import path
from crud.views import show_data, sign_in

urlpatterns = [
    path('show_data/', show_data, name='show_data'),
    path('sign_in/', sign_in, name='sign_in')
]
