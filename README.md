# Interview App API

## Overview
The Interview App API provides backend functionality for analyzing logistics data and providing meaningful insights. The project is designed to be scalable and follows the principles of the 12-factor methodology. This RESTful API is implemented using Django, Django REST Framework, and PostgreSQL.

## Installation

1. Clone the repository:
   git clone https://github.com/ahmet123/interview_app.git

2. Create a virtual environment:
   python -m venv .venv

3. Activate the virtual environment:

   - On Windows:
     .venv\Scripts\activate

   - On macOS/Linux:
     source .venv/bin/activate

4. Install the dependencies:
   pip install -r requirements.txt

5. Configure environment variables by creating a `.env` file:
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql://username:password@localhost:5432/interview_app
   DEBUG=True
   ALLOWED_HOSTS=*

6. Run migrations to set up the database:
   python manage.py migrate

7. Start the development server:
   python manage.py runserver

## API Endpoints

The following are the available API endpoints:

### Health Check
- `GET /health/`
  A simple health check to verify that the server is running.

### API Routes
- `GET /api/customers/`
  List all customers.
- `POST /api/customers/`
  Create a new customer.
- `GET /api/employee_details/`
  List all employee details.
- `POST /api/employee_details/`
  Create new employee details.
- `GET /api/shipments/`
  List all shipments.
- `POST /api/shipments/`
  Create a new shipment.
- `GET /api/payment_details/`
  List all payment details.
- `POST /api/payment_details/`
  Create new payment details.
- `GET /api/shipment_details/`
  List all shipment details.
- `POST /api/shipment_details/`
  Create new shipment details.
- `GET /api/employee_manages_shipment/`
  List all employee management of shipments.
- `POST /api/employee_manages_shipment/`
  Assign employee to manage a shipment.
- `GET /api/memberships/`
  List all memberships.
- `POST /api/memberships/`
  Create a new membership.
- `GET /api/status/`
  List all statuses.
- `POST /api/status/`
  Create a new status.
- `GET /api/routes/`
  List all routes.
- `POST /api/routes/`
  Create a new route.
- `GET /api/locations/`
  List all locations.
- `POST /api/locations/`
  Create a new location.
- `GET /api/users/`
  List all users.
- `POST /api/users/`
  Create a new user.
- `GET /api/deliveries/`
  List all deliveries.
- `POST /api/deliveries/`
  Create a new delivery.

### Custom Endpoints
- `GET /api/customers/count-by-type/`
  Count customers grouped by type.
- `GET /api/customers/count-by-payment-status/`
  Count customers grouped by payment status.
- `GET /api/customers/count-by-payment-mode/`
  Count customers grouped by payment mode.
- `GET /api/shipments/count-by-domain/`
  Count shipments grouped by domain.
- `GET /api/customers/membership-duration/`
  Count customers by their membership duration.

## Swagger UI
The API documentation is available in Swagger format. You can access it via:

- Swagger UI: http://localhost:8000/swagger/
- Redoc UI: http://localhost:8000/redoc/

## Running Tests
To run the tests, use the following command:
   python manage.py test