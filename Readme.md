# Тестовое задание: Система древовидных комментариев

## Используемые технологии
![](https://img.shields.io/badge/Python3-mediumblue) ![](https://img.shields.io/badge/Django-mediumvioletred) ![](https://img.shields.io/badge/DRF-black) ![](https://img.shields.io/badge/Nginx-purple) ![](https://img.shields.io/badge/Gunicorn-gold) ![](https://img.shields.io/badge/Docker-red) 

## Описание проекта
Проект предоставляет систему древовидных комментариев с системой регистрации и аутентификации на основе JWT-токенов.  

Объект публикации в представлении для клиента имеет следующие атрибуты:
* название публикации;
* автор публикации;
* дата публикации;
* текст публикации;
* изображение (необязательный);
* количество непосредственных комментариев.

Объект комментария в представлении для клиента имеет следующие атрибуты:
* автор комментария;
* дата публикации;
* текст комментария;
* изображение (необязательный);
* количество непосредственных комментариев.

Для получения данных дерева комментариев пользователю предоставляются следующие эндпоинты с приведенной структурой ответов на GET-запросы:

* `/api/v1/posts/` - данные по всем публикациям
```json
{
    "count": 7,
    "next": "http://<your_host>/api/v1/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Пост №1",
            "author": "admin",
            "image": null,
            "text": "Пост у которого 3 комментария",
            "pub_date": "2021-10-28T17:26:06.088000+03:00",
            "comments_count": 3
        },
        ...
        {
            ...
        }
    ]
}
```
* `/api/v1/posts/{post_id}/comments/` - данные по всем комментариям к конкретному посту, `/api/v1/comments/{comment_id}/comments/` - данные по всем комментариям к конкретному комментарию
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "admin",
            "image": null,
            "text": "Комментарий №1. Относится к посту №1 и имеет 3 свих комментария.",
            "pub_date": "2021-10-28T17:28:12.111000+03:00",
            "children_comments_count": 3
        },
        ...
        {
            ...
        }
    ]
}
```
Полный список доступных эдпоинтов с указанием реализуемых ими действий приведен в таблице 1.

Таблица 1 Доступные эндпоинты

Эндпоинт | Mетод | Действие | Права доступа
--- | --- | --- | ---
`/api/v1/auth/users/` | POST | создание нового пользователя | Any
`/api/v1/auth/jwt/create/` | POST | получение JWT-токена | User
`/api/v1/auth/jwt/refresh/` | POST | обновление JWT-токена | User
`/api/v1/users/me/` | GET | получение данных своей учетной записи | User
| | PATCH | изменение данных своей учетной записи | User
`/api/v1/posts/` | GET | получение списка всех публикаций | Any
| | POST | добавление новой публикации | User
`/api/v1/posts/{post_id}/` | GET | получение публикации | Any
| | PATCH | изменение публикации | User(author)
| | DELETE | удаление публикации | User(author)
`/api/v1/posts/{post_id}/comments/` | GET | получение списка всех комментариев к конкретному посту | Any
| | POST | добавление нового комментария к конкретному посту | User
`/api/v1/posts/{post_id}/ comments/{comment_id}/` | GET | получение комментария к посту| Any
| | PATCH | изменение комментария к посту| User(author)
| | DELETE | удаление комментария к посту| User(author)
`/api/v1/comments/{comment_id}/comments/` | GET | получение списка всех комментариев к родительскому комментарию | Any
| | POST | добавление нового комментария к родительскому комментарию | User
`/api/v1/comments/{comment_id}/ comments/{comment_id}/` | GET | получение комментария к родительскому комментарию | Any
| | PATCH | изменение комментария к родительскому комментарию | User(author)
| | DELETE | удаление комментария к родительскому комментарию | User(author)


## Требования
Для развертывания проекта описанным ниже способом на базе Linux должны быть установлены и включены утилиты docker и docker-compose. Для развертывания на базе Windows10 должны быть установлены запущены WSL2 и Docker-desktop.

## Как развернуть

1. Склонируйте репозиторий: ```https://github.com/palmage/blog```.
2. В директорию ```blog/``` в которой располагается файл настроек проекта settings.py добавьте файл ```.env``` и заполните его следующими переменными окружения:
```PowerShell
DJANGO_SECRET_KEY='<your_django_secret_key>'
HOST='<your_host>'

DB_ENGINE='django.db.backends.postgresql_psycopg2'
DB_NAME='postgres'
POSTGRES_USER='<your_db_username>'
POSTGRES_PASSWORD='<your_db_password>'
DB_HOST='db'
DB_PORT='5432'
```  
*с целью демонстрации проекта заполненный файл ```.env``` умышлено сохранен в публичном доступе

3. Из корневой директории проекта выполните команду ```sudo docker-compose up --build```.  
4. Примените миграции: ```sudo docker-compose exec web python manage.py migrate --noinput```.  
5. Cоберите статику: ```sudo docker-compose exec web python manage.py collectstatic --noinput```.  
6. Для наполнения БД начальными данными выполните команды:

```bash
sudo docker-compose exec web python3 manage.py shell 
```
```python
# выполнить в открывшемся терминале:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
```
```bash
sudo docker-compose exec web python manage.py loaddata fixtures.json
``` 
7. При необходимости создайте суперпользователя или воспользуйтесь учетными данными загруженными на предыдущем шаге из `fixtures.json`: login `admin`, password: ```admin```. Создать суперпользователя:   
```bash
sudo docker-compose exec web python manage.py createsuperuser
```  

## Как работать с API
Для работы с API подходят [CURL](https://losst.ru/kak-polzovatsya-curl) 
или [Postman](https://www.postman.com).  

Для прохождения аутентификации при работе с API передавайте в заголовкe `Authorization` JWT-токен в виде: `Bearer <access-токен>`.

### Регистрация пользователей и получение access-токена
Для регистрации пользователя отправьте POST-запрос с параметрами ```username``` и `password` на ```api/v1/auth/users/```.

После успешной регистрации для получения access-токена отправьте POST-запрос с параметрами ```username``` и `password` зарегестрированного пользователя на ```api/v1/auth/jwt/create/```
