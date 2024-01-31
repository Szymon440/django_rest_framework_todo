# Todo REST API with Django

This is a RESTful API for a Todo app built with Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Docker and Docker Compose installed on your machine to build and run the application.

### Installation & Running

Follow these steps to get the app running:

1. **Build the Docker image**

   Run the following command to build the Docker image: `docker-compose build`

2. **Start the Docker containers**

    Run the following command to start the Docker containers in detached mode: `docker-compose up -d`

3. **Apply migrations**

    Run the following command to apply the migrations: `python manage.py migrate`


## Endpoints
   Base url path `/api/tasks/`

   Get all Tasks
   `/api/tasks/` -> `GET`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/7607df73-0f3d-4418-8f1d-3647c1e40c87)
   
   Get specific Task
   `/api/tasks/id/`  -> `GET`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/09b65d82-a8d2-4da2-8e4b-de85dec4b6fd)
   
   Add Task
   `/api/tasks/`  -> `POST`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/5d00d608-cb7e-4ca7-a06a-f9defa25f401)
   
   Update task
   `/api/tasks/id/`  -> `PUT`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/88e21a53-6a99-43db-899a-4d9a6161bc29)

   Delete task
   `/api/tasks/id/`  -> `DELETE`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/f946da7b-e1e2-4231-9bf5-efe8cb675363)
