FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "main:app"]