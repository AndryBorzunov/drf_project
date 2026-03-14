from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__All__"


class LessonDivSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("name", "description", "preview")


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, obj):
        if obj.lessons.count():
            return obj.lessons.count()
        return 0

    class Meta:
        model = Course
        fields = ("name", "preview", "description", "lessons_count")


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonDivSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        if obj.lessons.count():
            return obj.lessons.count()
        return 0

    class Meta:
        model = Course
        fields = ("name", "preview", "description", "lessons_count", "lessons")
