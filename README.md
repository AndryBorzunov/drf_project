Django REST Framework

В проекте разрабатывается LMS-система на основе Django REST Framework

Созданы модели со следующими полями:

1. User (Пользователь) на базе AbstractUser. 
- авторизация заменена на email
- phone - телефон
- city - город
- avatar - аватарка пользователя

2. Course - курс
- name - название
- preview - превью 
- description - описание

3. Lesson - урок
- name - название
- description - описание
- preview - превью
- video_url - ссылка на видео
- course - привязка к учебному курсу

4. Для реализации CRUID для курса использован viewsets
5. Для реализации CRUID для урока - Generic-классы

6. Для работы контроллеров описаны простейшие сериализаторы
