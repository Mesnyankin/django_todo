from celery import shared_task
from .models import Task

@shared_task
def send_task_reminder(task_id):
    task = Task.objects.get(id=task_id)
    # Реализуйте логику напоминания
    print(f"Reminder: {task.title}")