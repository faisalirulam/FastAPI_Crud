# FastAPI CRUD Application

This is a FastAPI application with CRUD operations and database migrations using Alembic.

## Getting Started

### Prerequisites

- Python 3.9+
- FastAPI
- SQLAlchemy
- Alembic
- Uvicorn

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/faisalirulam/FastAPI_Crud.git
    cd FastAPI_Crud
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

To run the FastAPI application with Uvicorn:
```sh
uvicorn app.main:app --reload
```
### Database Migrations

Initialize Alembic

To create the Alembic folder and initialize the migration environment:
```sh
alembic init alembic
```

### Create Migrations

To generate a new migration script:
```sh
alembic revision --autogenerate -m "Initial migration"
```

### Apply Migrations
To apply the migrations to the database:
```sh
alembic upgrade head
```

### Check Running
To check app is running:
```sh
Visit on: http://127.0.0.1:8000
```

### Check Documentation
To check documentation of the project:
```sh
Visit on: http://127.0.0.1:8000/redoc
```

### Swagger UI
To check swagger UI or test apis:
```sh
Visit on: http://127.0.0.1:8000/docs
```
