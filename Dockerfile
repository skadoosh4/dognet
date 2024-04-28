FROM python:3.11-slim
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "gunicorn" , "--workers=4" , "--bind" , "0.0.0.0:8080" , "app:app"]