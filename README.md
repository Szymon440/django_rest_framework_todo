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

4. **Access the application**

    You can now access the application at: `http://localhost:8000/`



   
