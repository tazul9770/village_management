from django.contrib import admin
from django.urls import path, include
# from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.conf import settings
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('village/', include('village.urls')),
    path('users/', include('users.urls'))
] 
# + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
