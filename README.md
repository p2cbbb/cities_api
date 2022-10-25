# Тестовое задание по созданию HTTP API сервиса

### Задание 
>Реализовать сервис, который принимает и отвечает на HTTP запросы   

>Полный текст задания находится [по ссылке](https://drive.google.com/file/d/1DU2-MSCNN-FzCa8ksB3rx2GQy23LSt5T/)

### Функционал
1. В случае успешной обработки сервис должен отвечать статусом 200, в случае любой ошибки — статус 400.
2. Сохранение всех объектов в базе данных.
3. Запросы:
- `GET /city/` — получение всех городов из базы;    
- `GET /city/<int:city_id>/street/` — получение всех улиц города; (city_id — идентификатор города)    
- `POST /shop/` — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи.    
- `GET /shop/?street=<street>&city=<city>&open=0/1` — получение списка магазинов; 
> I. Метод принимает параметры для фильтрации. Параметры не обзательны. В случае отсутствия параметров выводятся все магазины, если хоть один параметр есть, то по нему выполнется фильтрация  
> II. Важно!: в объекте каждого магазина выводится название города и улицы, а не id записей    
> III. Параметр open: 0 - закрыт, 1 - открыт. Данный статус определется исход из параметров "Время открытия", "Время закрытия" и текущего времени сервера.   

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/p2cbbb/cities_api
cd cities_api
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Устанавливаем переменные окружения
В папке `config` создать файл `.env` и заполнить eго ключами

```bash
SECRET_KEY=<secret_key>
DEBUG=<debug>
DATABASE_NAME=<db_name>
DATABASE_USER=<db_user>
DATABASE_PASSWORD=<db_password>
DATABASE_HOST=<db_host>
DATABASE_PORT=<db_port>
```

### Применение миграций, создания суперпользователя и запуск проекта
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Запуск тестов
 
```bash
python -m pytest api/tests.py
```

### Команда для запуска проекта через docker
```bash
docker-compose up --build
```

### Эндпоинты
- `GET /api/city/` — получение всех городов из базы
##### Ответ:
```json
{
    "cities": [
        {
            "city_name": "Санкт-Петербург"
        },
        {
            "city_name": "Москва"
        },
        ...
    ]
}
```


- `GET /city/<int:city_id>/street/` — получение всех улиц города
##### Ответ:
```json
{
    "streets": [
        {
            "street_name": "Марата"
        },
        {
            "street_name": "Пушкинская"
        },
        ...
    ]
}
```

- `POST /shop/` — создание магазина  
##### Запрос:
```json
{
    "shop_name": "SoftMagic",
    "city": {
        "city_name": "Санкт-Петербург"
    },
    "street": {
        "street_name": "Марата"
    },
    "house": 8,
    "opening_time": "10:00:00",
    "closing_time": "22:00:00"
}
```
##### Ответ:
```json
{
    "shop_id": 2,
    "status": "ok"
}
```

- `GET /shop/?street=<street>&city=<city>&open=0/1` — получение списка магазинов
##### Ответ:
```json
{
    "shops": [
        {
            "shop_name": "SoftStore",
            "city": {
                "city_name": "Санкт-Петербург"
            },
            "street": {
                "street_name": "Марата"
            },
            "house": 12,
            "opening_time": "10:00:00",
            "closing_time": "22:00:00"
        },
        ...
    ]
}
```


