# dj-crud-docker

## To run the application locally: 

1. Clone the repository

1. Create a Virtual Environment: `python -m venv [vir-env-name]`

1. Activate the Virtual Environment: `[vir-env-name]\Scripts\Activate`

1. Install the requirements using the cmd: `pip install -r requirements.txt`

1. Run the django project: `python manage.py runserver`

## To run the Docker Image: 
A Docker Image of this application exists on Docker Hub

Docker command to pull and run the image as a container: 

`docker run -dp 0.0.0.0:8000:8000 abhishekganji27/django-crud:v3`
