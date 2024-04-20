# anverali_test_task

---
**О проекте:**
- Cайт с админ панелью и 2-мя кабинетами заказчика и исполнителя.
- Поля в моделях заказчика и исполнителя:
    - Имя
    - Фамилия
    - Телефон(валидация на вводимую информацию)
    - Почта(валидация на вводимую информацию)
    - Опыт
- Библиотеки которые использовались при написании проекта находятся в requirements.txt
---
**Разворачивание проекта:**
- `git clone https://github.com/AliaksandrSihai/anverali_test_task`
- создать базу данных и файл .env(образец необходимых зависимостей находятся в .env_sample) и добавить необходимые переменные
- `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- `python manage.py makemigrations && python manage.py migrate `
- Для создания админ-пользователя выполнить команду  `python manage.py csu`
- `python manage.py runserver`
---
**Стек**:
- Python
- Django
- PostgreSQL
___
**О проекте:**
- Cайт с админ панелью и 2-мя кабинетами заказчика и исполнителя.Набор полей в профилях (имя,фамилия, контактные данные, опыт). БД PostgreSQL
