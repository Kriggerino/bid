FROM python:3.10.13-slim
RUN apt update
RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD metadata.py /app
ADD reader.py /app
ADD main.py /app
ADD .env /app/
EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]