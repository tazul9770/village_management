from django.db import models
from django.conf import settings

class Village(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    address = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username} Profile"
    
class Complain(models.Model):
    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('resolved', 'RESOLVED'),
        ('rejected', 'REJECTED')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conplains')
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='complaint_image/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    complaint = models.ManyToManyField(Complain, related_name='tags', blank=True)

    def __str__(self):
        return self.name
    
class ComplainResponse(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE, related_name='responses')
    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Response by {self.responder} on {self.complaint.title}" 
