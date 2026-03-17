import re
from rest_framework import serializers


class VideoUrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # Регулярное выражение для YouTube-ссылок
        reg = re.compile(
            r"(https?://)"  # протокол
            r"(www\.)?"  # www
            r"(youtube|youtu|youtube-nocookie)\.com/"  # домен
            r"(watch\?v=|embed/|v/|shorts/|)"  # пути
            r"([\w-]{11})"  # ID видео (11 символов)
            r"(&\S*)?"  # дополнительные параметры
            r"$"
        )

        tmp_val = dict(value).get(self.field)
        if not reg.search(tmp_val):
            raise serializers.ValidationError("Некорректная ссылка на YouTube")
        return value
