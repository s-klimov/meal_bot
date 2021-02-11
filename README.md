#### Материалы, используемые при написании кода 
[Описание структуры проекта](https://telegra.ph/Novaya-struktura-dlya-bota-na-baze-aiogram-11-27)  
[Создание модели данных и миграции](https://telegra.ph/Migracii-baz-dannyh-gino--alembic-11-29)  
[Использование Middlwares в aiogram](https://telegra.ph/Ispolzovanie-Middlwares-v-aiogram-08-14)

#### Подготовка проекта к запуску
1. Установка PostgreSQL
1. Установка библиотеки для чтения QR-кодов  
    * $ `sudo apt-get install libzbar0`
1. Создать миграции 
    1. Установить [poetry](https://python-poetry.org/docs/#installation) в операционную систему
    1. Переходим в корень проекта
    1. $ `poetry init`
    1. $ `poetry add aiogram environs loguru gino alembic psycopg2-binary`
    1. Добавить в файл pyproject.toml  
       `[tool.poetry] packages = [{ include = "app" }]`   
    1. $ `poetry install`
    1. $ `poetry shell`
    1. Создаем миграции  
       $ `poetry run alembic revision -m "first migration" --autogenerate`  
    1. Применяем миграции  
       $ `alembic upgrade head`

#### Запуск проекта
1. $ `python -m app`

#### Как управлять подключением к серверву из консоли/терминала
1. скачать у поставщика услуги виртуального сервера pem-файл
1. выполнить над pem-файлом команду $ `chmod 400 mykey.pem` [400 protects it by making it read only and only for the owner](https://stackoverflow.com/questions/8193768/trying-to-ssh-into-an-amazon-ec2-instance-permission-error)
1. Подключение к серверу  $ `ssh -i /home/klimov/PycharmProjects/amazon_server/amazonserver.pem ubuntu@18.222.18.171`
1. Копирование файлов с компьютера на сервера  $ `scp -i /home/klimov/PycharmProjects/amazon_server/amazonserver.pem -r /home/klimov/PycharmProjects/k-bot-2 ubuntu@18.222.18.171:/home/ubuntu
`