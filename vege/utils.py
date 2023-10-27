from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client():
    send_mail(
        subject='VegeApp',
        message='Vege from django',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['pranshujain0331@gmail.com'],
    )
