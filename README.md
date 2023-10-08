## Django + FastAPI Microservice App with RabbitMQ

This is a microservice application built using Django, FastAPI, and RabbitMQ. The Django application serves as an admin panel for managing products, while the FastAPI app allows users to like products. The application uses RabbitMQ as a message broker for communication between the microservices.

### Architecture

The backend is composed of two apps:

- **Admin App**: Built using Django, it handles the creation, updating, and deletion of products.
- **Main App**: Built using FastAPI, it allows users to like products.

### Technologies Used

- Django
- FastAPI
- RabbitMQ
- Railway MySQL (DBaaS for Django)
- Atlas MongoDB (DBaaS for FastAPI)

### Setup

1. Clone the repository:

```shell
git clone https://github.com/your-username/your-repo.git
```

2. Install the required dependencies for both Django and FastAPI:

```shell
pip install -r django/requirements.txt
pip install -r fastapi/requirements.txt
```

3. Configure the database connections:

- For Django, update the `DATABASES` setting in the `django/settings.py` file to use your Railway MySQL database.
- For FastAPI, update the MongoDB connection string in the `fastapi/main.py` file to use your Atlas MongoDB database.

4. Start the microservices:

- For the Django admin app, run the following command in the `django/` directory:

```shell
python manage.py runserver
```

- For the FastAPI main app, run the following command in the `fastapi/` directory:

```shell
uvicorn main:app --reload
```

5. Access the applications:

- The Django admin app can be accessed at `http://localhost:8000/admin/`.
- The FastAPI main app can be accessed at `http://localhost:8000/`.

### Communication between Microservices

The microservices communicate with each other using RabbitMQ. The Django admin app sends messages to the RabbitMQ exchange, and the FastAPI main app consumes these messages to update the likes count for a product.

### Docker

Both the Django and FastAPI microservices have their respective Docker images uploaded to Docker Hub. You can use the following commands to run the application using Docker:

- For the Django admin app:

```shell
docker run -p 8000:8000 your-dockerhub-username/django-microservice:latest
```

- For the FastAPI main app:

```shell
docker run -p 8000:8000 your-dockerhub-username/fastapi-microservice:latest
```

### Conclusion

This microservice application demonstrates the integration of Django and FastAPI using RabbitMQ as a message broker. The Docker images for both microservices allow for easy deployment and scaling in a production environment.