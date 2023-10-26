FROM python:3.8-alpine
COPY . /app
COPY .env /app/.env
WORKDIR /app
RUN pip3 install -r ./requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
