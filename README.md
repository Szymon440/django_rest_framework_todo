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
   `/`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/9fdf12ff-66d4-429e-b551-c0fdb9f6e710)
   `addTask`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/c62c3008-0782-416d-8f3c-431f0fdc1de1)
   `updateTask/id`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/27f3f243-a66d-457e-a123-9fadaae19456)
   `deleteTask/id`
   ![image](https://github.com/Szymon440/django_rest_framework_todo/assets/75849710/26ee53fb-17e0-46ce-a9af-2e0ac6e5825a)
