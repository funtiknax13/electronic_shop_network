# Api приложения сети по продаже электроники 

Технологии
```
* Python
* Django, DRF
* JWT, DRF-YASG
* PostgreSQL
```

Для запуска необходимо создать файл .env в папке проекта и задать следующие переменные:
```
SECRET_KEY=
DEBUG=
DB_PASSWORD=
```

Документация:
```
/swagger/
/redoc/
```

Для создания образа из Dockerfile и запуска контейнера:
```
docker compose up --build
```

Для запуска приложения:
```
python3 manage.py runserver
```


