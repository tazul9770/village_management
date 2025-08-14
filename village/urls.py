from django.urls import path
from village.views import complain, create_village, dashboard, complain_detail, update_complain, delete_complain, village_information, update_village, delete_village, give_response, admin_dashboard, assign_staff, remove_staff, delete_user

urlpatterns = [
    path('complain/', complain, name='complain'),
    path('update_complain/<int:user_id>', update_complain, name='update_complain'),
    path('complain_detail/<int:user_id>/', complain_detail, name='complain_detail'),
    path('delete_complain/<int:complain_id>/', delete_complain, name='delete_complain'),
    path('give_response/<int:complain_id>/', give_response, name='give_response'),
    path('create_village/', create_village, name="create_village"),
    path('update_village/<int:village_id>/', update_village, name='update_village'),
    path('delete_village/<int:village_id>/', delete_village, name='delete_village'),
    path('village_information/', village_information, name='village_information'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('assign_staff/<int:user_id>/', assign_staff, name='assign_staff'),
    path('remove_staff/<int:user_id>/', remove_staff, name='remove_staff'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user')
]
