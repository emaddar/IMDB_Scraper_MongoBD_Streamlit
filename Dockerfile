# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8505/_stcore/health

ENTRYPOINT ["streamlit", "run", "Films.py", "--server.port=8505", "--server.address=0.0.0.0"]

# docker build -t imdb .
# docker run -p 8505:8505 imdb