# Указываем базовый образ для Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из текущей директории на локальной машине в контейнер
COPY . /app/

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска FastAPI с помощью Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]