# Khanto Reservation System

A reservation system for Khanto's properties, built with Python, Django, Django Rest Framework, Postgres and Docker.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- Django
- Django Rest Framework
- Postgres
- Docker
- pytest

### Installing

1. Clone the repository:
'git clone https://github.com/lucasribeirorsousa/carford-app.git'

2. Run project
'docker-compose up'

3. Execute tests
'pytest path/'

### API Endpoints

#### Properties

- `GET /properties/`: Retrieve a list of properties.
- `GET /properties/<property_id>/`: Retrieve a specific property.
- `POST /properties/`: Create a new property.
- `PUT /properties/<property_id>/`: Update an existing property.
- `DELETE /properties/<property_id>/`: Delete a property.

#### Advertisements

- `GET /ads/`: Retrieve a list of advertisements.
- `GET /ads/<ad_id>/`: Retrieve a specific advertisement.
- `POST /ads/`: Create a new advertisement.
- `PUT /ads/<ad_id>/`: Update an existing advertisement.

#### Reservations

- `GET /reservations/`: Retrieve a list of reservations.
- `GET /reservations/<reservation_id>/`: Retrieve a specific reservation.
- `POST /reservations/`: Create a new reservation.
- `DELETE /reservations/<reservation_id>/`: Delete a reservation.

## Built With

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Postgres](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [pytest](https://docs.pytest.org/en/latest/)

## Authors

* **Lucas Ribeiro** - *Initial work* - [Your Github](https://github.com/lucasribeirorsousa)

## License

This project is licensed under the MIT License