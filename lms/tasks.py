from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_subscript(emails, course_id, name):
    print(emails)
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
