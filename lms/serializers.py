from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lms.models import Course, Lesson, Subscription
from lms.validators import VideoUrlValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [VideoUrlValidator(field="video_url")]


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
        fields = ("id", "name", "preview", "description", "lessons_count", "owner")


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonDivSerializer(many=True, read_only=True)
    is_subscript_enable = SerializerMethodField()

    def get_lessons_count(self, obj):
        if obj.lessons.count():
            return obj.lessons.count()
        return 0

    def get_is_subscript_enable(self, obj):
        request = self.context.get("request")

        for user_item in list(obj.subscription.values_list("user", flat=True)):
            if user_item == request.user.id:
                return True
        return False

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "preview",
            "description",
            "lessons_count",
            "lessons",
            "is_subscript_enable",
        )


class SubscriptionSerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = ["user", "course"]
