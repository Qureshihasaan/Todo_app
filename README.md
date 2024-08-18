# Todo App

This is a simple and efficient ToDo application built using FastAPI, SQLModel, Docker, and Cloudflare. The application allows users to create, update, delete, and manage their tasks with ease.

## Features
* FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
* SQLModel: A SQL-friendly ORM (Object Relational Mapper) built on top of SQLAlchemy and Pydantic.
* Docker: Containerization of the application to ensure portability and easy deployment.
* Cloudflare: Used for DNS management and ensuring the app is served securely with HTTPS.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- You have installed Docker.
- You have installed Python 3.8+.
- You have a Cloudflare account for DNS management.

## Installation
1. Clone the Repository
    git clone https://github.com/Qureshihasaan/Todo-app
    cd Todo-app
2. Set Up Environment Variables
Create a .env file in the root of your project and add the necessary environment variables:

3. Build and Run the Application Using Docker

    docker-compose up --build

4. Apply Database Migrations
- Once the containers are up and running, apply the necessary database migrations:

5. Access the Application
- Your ToDo app should now be running and accessible. Navigate to http://localhost:8000 to view the application.

## Usage
* Create a Task: Use the POST /tasks/ endpoint to create a new task.
* Get All Tasks: Use the GET /tasks/ endpoint to view all tasks.
* Update a Task: Use the PUT /tasks/{task_id} endpoint to update a specific task.
* Delete a Task: Use the DELETE /tasks/{task_id} endpoint to delete a specific task.