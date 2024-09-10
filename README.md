# Приложение для управления продуктами

Это простое Django-приложение для управления продуктами с помощью RESTful API и фронтенд-интерфейса, построенного на HTML и JavaScript. Приложение позволяет пользователям создавать и просматривать продукты через форму и динамически отображать список продуктов.



### Объяснение структуры README

1. **Введение и функциональные возможности**: Описание основного назначения и возможностей приложения.
2. **Технологии**: Указаны используемые технологии и инструменты.
3. **Предварительные требования**: Объяснение, что необходимо для запуска проекта.
4. **Начало работы и установка**: Подробное руководство по установке и настройке проекта.
5. **Использование**: Инструкции по использованию приложения.
6. **Конечные точки API**: Описание доступных API и примеров запросов.
7. **Запуск тестов**: Команды для тестирования приложения.
8. **Участие в проекте**: Как можно внести свой вклад в проект.
9. **Лицензия и благодарности**: Информация о лицензии и благодарности. 

## Функциональные возможности

- **RESTful API**: Предоставляет конечные точки для создания и получения списка продуктов.
- **Фронтенд интерфейс**: Удобная HTML-страница с формой для добавления новых продуктов и отображения списка продуктов с использованием JavaScript и AJAX (Fetch API).
- **Проверка данных**: Обеспечивает валидацию всех вводимых данных (например, название не может быть пустым, цена должна быть положительным числом).
- **Минимальная стилизация**: Использует Bootstrap для базового стиля, чтобы улучшить внешний вид интерфейса.

## Технологии

- **Бэкенд**: Django, Django REST Framework
- **Фронтенд**: HTML, JavaScript, Bootstrap
- **База данных**: SQLite (по умолчанию в Django)

## Предварительные требования

Убедитесь, что на вашем компьютере установлены следующие компоненты:

- Python 3.x
- pip (инструмент для установки пакетов Python)
- Виртуальное окружение (опционально, но рекомендуется)

## Начало работы

Следуйте этим инструкциям, чтобы получить копию проекта и запустить его на вашем локальном компьютере для разработки и тестирования.

### Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/yourusername/product-management-app.git
    cd product-management-app
    ```

2. **Создайте и активируйте виртуальное окружение:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Запустите миграции для настройки базы данных:**

    ```bash
    python manage.py migrate
    ```

5. **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

6. **Откройте приложение в браузере:**

    Перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), чтобы увидеть интерфейс фронтенда.

### Использование

- Используйте форму на главной странице для добавления новых продуктов.
- Список продуктов автоматически обновляется после успешного добавления.
- Продукты отображаются в динамически генерируемой таблице под формой.

### Конечные точки API

- **GET /api/products/**: Получить список всех продуктов.
- **POST /api/products/**: Добавить новый продукт (ожидает JSON с `name`, `description` и `price`).

### Пример JSON для POST-запроса

```json
{
  "name": "Пример продукта",
  "description": "Описание примерного продукта.",
  "price": 19.99
}
