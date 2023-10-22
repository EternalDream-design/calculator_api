# Образ python
FROM python:3.11-slim

# Установка зависимостей
RUN pip install Flask==3.0.0 flask_cors==3.0.10 --no-cache-dir

#Создание рабочей директории
WORKDIR /app

#Копирование python файла
COPY calc_api_appsec.py .

#Порт, который прослушивает приложение
EXPOSE 5000

#Скрипт, выполняющийся при запуске контейнера
CMD ["python", "calc_api_appsec.py"]

USER 1000
