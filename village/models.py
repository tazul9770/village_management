from django.db import models
from django.conf import settings
from django.utils import timezone

class Village(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    post_code = models.CharField(max_length=20, default='0000')
    image = models.ImageField(upload_to='village_images/', blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    total_voters = models.IntegerField(default=0)  
    area_sq_km = models.FloatField(blank=True, null=True, help_text="Village area in square kilometers")
    head_of_village = models.CharField(max_length=100, blank=True, null=True)
    literacy_rate = models.DecimalField(max_digits=5,decimal_places=2,default=0.00,
        help_text="Percentage of literate people in the village"
    )
    established_year = models.IntegerField(blank=True, null=True)
    number_of_houses = models.IntegerField(blank=True, null=True)
    number_of_schools = models.IntegerField(blank=True, null=True)
    number_of_health_centers = models.IntegerField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text="Upload a profile picture"
    )
    phone = models.CharField(max_length=25, blank=True)
    bio = models.TextField(blank=True, default='')
    def __str__(self):
        return f"{self.user.username} Profile"
    
class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name
    
class Complain(models.Model):
    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('resolved', 'RESOLVED'),
        ('rejected', 'REJECTED')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complains')
    tags = models.ManyToManyField(Tag, related_name='complaints', blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='complaint_image/', blank=True, null=True, default='images/default.png')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
class ComplainResponse(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE, related_name='responses')
    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Response by {self.responder} on {self.complain.title}" 
