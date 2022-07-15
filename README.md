![1](https://github.com/alklim912/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# api_yamdb
# Проект «YaMDb»

## Описание:
Проект YaMDb собирает отзывы пользователей на произведения, которые, в свою очередь, делятся на категории: «Книги», «Фильмы», «Музыка» и тд.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

## Применяемые технологии / пакеты:
Принципы REST API.
Формат передачи данных - JSON.
Framework - Django, Django REST Framework.
JWT - Simple JWT.
DataBase - SQLite3.
Пакет datetime.
Модуль Requests.
Docker, docker-compose.
Gunicorn.
Nginx.
Наполнение базы тестовыми данными из CSV файлов.
Передача данных осуществляется по протоколу HTTP.  
Аутентификация осуществляется по JWT-токену.
#### Документация к API доступна по адресу `http://127.0.0.1/redoc/`

### Процесс регистрации новых пользователей:
1. Пользователь отправляет запрос с параметрами *email* и *username* на **/api/v1/auth/signup/**.  
2. Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный email-адрес.
3. Пользователь отправляет запрос с параметрами *username* и *confirmation_code* на эндпоинт **/api/v1/auth/token/**, в ответе на запрос ему приходит *token* (JWT-токен).
После регистрации и получения токена пользователь может отправить PATCH-запрос на **/users/me/** и заполнить поля в своём профайле (описание полей — в документации). 

### Шаблон наполнения env-файла:

 DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
 DB_NAME=<имя базы данных>
 POSTGRES_USER=<логин для подключения к базе данных>
 POSTGRES_PASSWORD=<пароль для подключения к БД>
 DB_HOST=<название сервиса (контейнера)>
 DB_PORT=<порт для подключения к БД>
 SECRET_KEY=<значение ключа из файла settings.py>

## Процесс установки:

 Клонируем репозиторий и переходим в него через терминал:

 ```$ git clone https://github.com/alklim912/api_yamdb.git```
 ```$ cd infra```

 Запускаем docker-compose:
 
 ```$ docker-compose up```
 ```$ source venv/bin/activate```
 
 Выполняем миграции, создаем админа, переносим статику в контейнере приложения:

 ```$ docker-compose exec web python manage.py migrate```
 ```$ docker-compose exec web python manage.py createsuperuser```
 ```$ docker-compose exec web python manage.py collectstatic --no-input```


## Пример использования API:

**GET /titles/** - получить список всех произведений  

Удачное выполнение запроса (200):
Ключ|Значение|Описание
----|--------|--------
"id"|integer|ID произведения
"name"|"string"|Название
"year"|integer|Год выпуска
"rating"|integer|Рейтинг на основе отзывов
"description"|"string"|Описание
"genre"|Array of objects|Жанр
||"name"|Название жанра (string)
||"slug"|"slug" (string)
"category"|object|Категория
||"name"|Название категории (string)
||"slug"|"slug" (string)

### Разработчик: [Александр Климентьев](https://github.com/alklim912)