from celery import shared_task
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .models import Notes

@shared_task
def send_mail_task():
    current_time = timezone.now()
    one_day_ago = current_time - timedelta(days=1)
    overdue_tasks = Notes.objects.filter(due_date__gte=one_day_ago, due_date__lt=current_time)

    for task in overdue_tasks:
        subject = f'Due Date Exceeded: {task.title}'
        message = f'The due date for task "{task.title}" has been exceeded.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['codedeveloper47@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )

    return "Mail has been sent........"