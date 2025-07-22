FROM python:3.12-slim
LABEL authors="zidan"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--chdir", "todo_list", "todo_list.wsgi:application", "--bind", "0.0.0.0:8000"]

