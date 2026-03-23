from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course, Lesson, Subscription
from users.models import User


class LessonAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="andry@mail.ru")
        self.course = Course.objects.create(
            name="Вышивание крестиком",
            description="Курс для обучения вышиванию крестиком",
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name="Урок 1",
            description="Основные моменты",
            course=self.course,
            owner=self.user,
        )
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("lms:lessons_create")
        data = {
            "name": "Урок 2",
            "course": self.course.pk,
            "description": "Основные методы",
            "video_url": "https://www.youtube.com/watch?v=ON9P6JnY4sU&ysclid=mmsms47wsd596616204",
        }
        response = self.client.post(url, data)
        # print(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Урок 3",
            "description": "Основные методы",
            "video_url": "https://www.youtube.com/watch?v=ON9P6JnY4sU&ysclid=mmsms47wsd596616204",
        }
        response = self.client.put(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Урок 3")

    def test_lesson_delete(self):
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": "Урок 1",
                    "description": "Основные моменты",
                    "preview": None,
                    "video_url": "",
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_course_retrieve(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("is_subscript_enable"), True)

    def test_subscription_create(self):
        url = reverse("lms:subscription")
        data = {"course_id": self.course.pk}
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("message"), "Подписка удалена")
