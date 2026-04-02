from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_subscript(emails, course_id, name):
    """Отправляет сообщение подписчикам об обновлении курса"""

    subject = f"Обновление курса {course_id}"
    message = f"Обновился учебный курс {name}"
    for recipient in emails:
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=[recipient],
                fail_silently=False,
            )

        except Exception as e:
            print(f"Ошибка отправки: {e}")


@shared_task
def disable_inactive_users():
    """Отключает пользователей, которые были неактивны более 1 месяца"""

    filter_data = timezone.now().date() - timedelta(days=30)
    inactive_users = User.objects.filter(is_active=True).exclude(
        last_login__isnull=False, last_login__gte=filter_data
    )

    for user_item in inactive_users:
        print(f"{user_item.email} : {user_item.is_active} : {user_item.last_login}")
        user_item.is_active = False
        user_item.save()
