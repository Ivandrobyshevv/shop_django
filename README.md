### Онлайн магазин Django

Возможности клиента:
* Регистрация(авторизация) пользователя
* Добавления товара в корзину
* Отслеживание товаров в корзине, редактирование их количества
* Работа с личным кабинетом (смена аватарки, редактирование личных данных)
* Просмотр категорий и полного списка товаров

### Установка
```bash
. env/bin/activate
pip3 install -r requirements.txt
python3 manage.py loaddata db.json
python3 manage.py runserver 8000
```

