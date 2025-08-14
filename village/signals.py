from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from village.models import ComplainResponse

@receiver(post_save, sender=ComplainResponse)
def response_mail(sender, instance, created, **kwargs):
    if created:
        subject = 'See your complain response'
        message = f"Hello {instance.complain.user.first_name},\n\nI am {instance.responder.first_name if instance.responder else 'Admin'}\n\n\n{instance.message}\n\n\nThanks {instance.complain.user.first_name}"
        recipient_list = [instance.complain.user.email]

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False
        )
