Eternal Elegance - Интернет-магазин одежды

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
Краткое, но емкое описание проекта на 1-2 предложения. Отвечает на вопросы:
* Что это? (интернет-магазин одежды на Flask с полным циклом онлайн-продаж)
* Для чего? (Проект включает каталог товаров, корзину, регистрацию)
Быстрый старт

Предварительные требования

- Python 3.8 или выше
- Установленный pip

### Установка и запуск
    * git clone https://github.com/Sofia-claire/aveline.git 
* cd aveline
* python -m venv venv
* python -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt
* cd aveline
* python app.py
Приложение будет доступно по ссылке:    file:///C:/Users/Пользователь/Desktop/shop/templates/index.html
Функциональность

 Покупательская зона

· Главная страница 
· Корзина покупок 
· Избранное 
· Регистрация
Структура проекта

aveline/
* ├── app.py                 # Основное приложение Flask
*  │   └── product1.jpg            # фотокарточка 1 продукта
*  │   └── product2.jpg            # фотокарточка 2 продукта
*  │   └── product3.jpg            # фотокарточка 3 продукта
*  │   └── product4.jpg            # фотокарточка 4 продукта    
*  └── templates/                  # HTML шаблоны
*  └── templates/                  # HTML шаблоны
*      ├── index.html              # Главная страница
*      ├── proba.html              # пробный бд
Технологический стек

Бэкенд:

· Python 3.8+
· Flask 2.0+
· Flask-Session
· SQLite3

Фронтенд:

· HTML CSS
Для добавления товаров используйте Flask shell или прямое редактирование базы данных. Пример добавления товара:

python
from app import app, db, Product

with app.app_context():
    new_product = Product(
        name="Платье летнее",
        description="Легкое летнее платье",
        price=2999,
        brand="Summer Collection",
        image="dress.jpg")
        ##  Документация

*   [Часто задаваемые вопросы (FAQ)]https://github.com/m0884

---

Лицензия

Распространяется под лицензией MIT. См. файл LICENSE для деталей.
 Контакты

m0884 на гитхабе
почта - mlanagudina@gmail.com ss
