FROM python:3.9.2-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# EXPOSE 8000/tcp

COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]

# VOLUME "./db:/app/db"
