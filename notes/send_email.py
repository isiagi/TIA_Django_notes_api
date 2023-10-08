from django.core.mail import EmailMessage
from django.conf import settings

def send(subject, message, recipients):
    return EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to=recipients)