FROM python:3.12.1-alpine

WORKDIR /app

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

EXPOSE 8000/tcp

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]