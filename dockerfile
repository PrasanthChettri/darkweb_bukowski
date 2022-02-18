FROM python:3.8
ENV DockerHOME=/home/app/webapp  
RUN mkdir -p $DockerHOME  
COPY . ${DockerHOME}
WORKDIR $DockerHOME  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
COPY . ${DockerHOME}
EXPOSE 8000  
CMD python manage.py runserver  