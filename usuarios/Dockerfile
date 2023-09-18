FROM alpine:3.14

RUN apk add py3-pip
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app/
  
RUN pip install --ignore-installed -r requirements.txt

EXPOSE 5000

CMD ["python3", "application.py"]