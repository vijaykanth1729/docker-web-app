FROM python:3
EXPOSE 8000
RUN mkdir -p /home/app
COPY . /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt
CMD ["python3","./manage.py","runserver", "0.0.0.0:8000"]
