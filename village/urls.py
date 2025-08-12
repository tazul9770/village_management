from django.urls import path
from village.views import complain, create_village, dashboard, complain_detail, update_complain

urlpatterns = [
    path('complain/', complain, name='complain'),
    path('update_complain/<int:user_id>', update_complain, name='update_complain'),
    path('complain_detail/<int:user_id>/', complain_detail, name='complain_detail'),
    path('create_village/', create_village, name="create_village"),
    path('dashboard/', dashboard, name='dashboard')
]
