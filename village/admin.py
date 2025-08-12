from django.contrib import admin
from village.models import Complain, ComplainResponse, Village, UserProfile

admin.site.register(Complain)
admin.site.register(ComplainResponse)
admin.site.register(Village)
admin.site.register(UserProfile)
