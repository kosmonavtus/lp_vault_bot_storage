# Прототип программы для храрения "секреетов"
Назавем ее LP27_Vault.
Софтинка создана в акакдемических целях.

Умеет записывать показывать и удалять информацию из BD.
Спомощью SQLAlchemy ORM.
Отдает "наружу" /location_name за которыми API методы для работы с БД.

## Захотелось написать readme.
### Ну напищем чтоыб было красиво.

Устанавливаем зависимости.
```
pip install -r requirements
```

В конфиге задаем значение переменной CONNECTION_STRING для подключения к БД.
```
CONNECTION_STRING = "CONNECTION_YOUR_STRING_VALUE"
./app/config.toml
```

Инициализируем базу отсюда.
Прото так она не инитнится, это надо переделать.
```
app/db_model.py
```

Запускаем софтинку из корня репозитория.
```
flask  --debug run
```

### Как жиьт когда у тебя, ну такое себе API?

Получить пользователя по ID:
```
curl -X GET  http://127.0.0.1:5000/users/user?user_id=10
```

Добавить нового пользователя:
```
curl -X POST -d '{"name": "test_views", "login":"test_views_login", "password":"test_create_user_password"}' -H 'Content-Type: application/json'  http://127.0.0.1:5000/users/add_user
```

Удалить пользователя:
```
curl -X POST -d '{"user_id": "71"}' -H 'Content-Type: application/json'  http://127.0.0.1:5000/users/delete_user
```

Получить "секрет" по ID:
```
curl -X GET  http://127.0.0.1:5000/repo/sh_secret?secret_id=10
```

Добавить секрет:
```
curl -X POST -d '{"name": "secret_name", "user_id": "72", "secret_type": "1"}' -H 'Content-Type: application/json'  http://127.0.0.1:5000/repo/add_secret
```

Удалить секрерт по ID секрета:
```
curl -X POST -d '{"secret_id": "58"}' -H 'Content-Type: application/json'  http://127.0.0.1:5000/repo/delete_secret

```

