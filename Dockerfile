FROM python:3
EXPOSE 8000
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code
