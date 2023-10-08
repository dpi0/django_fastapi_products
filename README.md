# Django + FastAPI Microservice Products App 

This microservice app consists of two main components: a Django admin app and a FastAPI app. The Django app is responsible for managing products, including their creation, updation, and deletion. The FastAPI app allows users to like a product.

## Technologies Used

- Django
- FastAPI
- RabbitMQ
- Railway MySQL (DBaaS)
- MongoDB Atlas (DBaaS)

## Usage

### Django Admin App

The Django admin app can be accessed at `http://localhost:7000/`. Use the admin interface to manage products.

### FastAPI App

The FastAPI app provides an endpoint for liking a product. Send a PUT request to `http://localhost:6969/products/{product_id}/like` to like a product, where `{product_id}` is the ID of the product to be liked.

## References

- [Building a CRUD App with FastAPI and MongoDB - TestDriven.io][1]
- [FastAPI MongoDB REST API w/ Python and PyMongo - YouTube][2]
- [FastAPI MongoDB Integration: 5 Easy Steps - Hevo Data][3]
- [Full Stack FastAPI, React, and MongoDB Build Python Web Applications With The FARM Stack PDF | PDF - Scribd][4]
- [Building Python Microservices with FastAPI, published by Packt - GitHub][5]
- [Re-Doing the Django Tutorial With FastAPI and React: Database & Models - dev.to][6]