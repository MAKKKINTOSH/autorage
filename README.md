# autorage
____________
## Инструкция по запуску в локальной сети:
(Проект работает на Python 3.11)

1. Клонировать репозиторий.
2. Cоздать виртуальное окружение следующей командой:
   `py -m venv venv`
3. Активировать виртуальное окружение командой:
   `venv/scripts/activate`
4. Установить зависимости с помощью команды:
   `py -m pip install -r requirements.txt`
5. Провести необходимые миграции с помощью команд
   сначала `py manage.py makemigrations` и `py manage.py migrate`
6. Запустить проект с помощью `py manage.py runserver`
