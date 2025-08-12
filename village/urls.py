from django.urls import path
from village.views import complain, create_village, dashboard

urlpatterns = [
    path('complain/', complain, name='complain'),
    path('create_village/', create_village, name="create_village"),
    path('dashboard/', dashboard, name='dashboard')
]
