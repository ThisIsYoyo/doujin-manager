FROM python:3.10.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r ./doujin_manager/requirements.txt

EXPOSE 8000
CMD ["sh", "-c", "python doujin_manager/manage.py migrate ; python doujin_manager/manage.py runserver 0.0.0.0:8000"]
