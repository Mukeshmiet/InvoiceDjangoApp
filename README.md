# Django Rest Framework Invoice Application

This is a Django application built using Django Rest Framework for managing invoices and their details. It provides API endpoints for creating, reading, updating, and deleting invoices and invoice details.

## Features

- Create, Read, Update, and Delete (CRUD) operations for invoices and invoice details.
- APIs to manage invoices and their associated details.
- Supports listing and viewing individual invoices and details.

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Mukeshmiet/InvoiceDjangoApp.git


Certainly! Here's the README.md file with proper formatting, including headers, bullet points, and other symbols:

markdown
Copy code
# Django Rest Framework Invoice Application

This is a Django application built using Django Rest Framework for managing invoices and their details. It provides API endpoints for creating, reading, updating, and deleting invoices and invoice details.

## Features

- Create, Read, Update, and Delete (CRUD) operations for invoices and invoice details.
- APIs to manage invoices and their associated details.
- Supports listing and viewing individual invoices and details.

## Setup Instructions

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/django-invoice-app.git

### Navigate to the project directory:

cd djangoInvoices

### Create a virtual environment (optional but recommended):

python -m venv venv

### Activate the virtual environment:

#### On Windows:

venv\Scripts\activate

#### On macOS and Linux:

source venv/bin/activate

### Install the project dependencies:

pip install -r requirements.txt

### Run migrations to create the database tables:

python manage.py makemigrations

python manage.py migrate

### Start the development server:

python manage.py runserver

#### Access the API at http://127.0.0.1:8000/api/invoices.
#### Access the API at http://127.0.0.1:8000/api/invoice_details.

### API Endpoints

#### /api/invoices/: Endpoint for managing invoices.
#### /api/invoice_details/: Endpoint for managing invoice details.

## Tests

To run the tests for this application, use the following command:

#### python manage.py test

The test cases are defined in the tests.py file and cover creating, updating, reading, and deleting invoices and invoice details.

### In tests.py

Import necessary modules
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

Rest of the tests.py content...

#### In the tests.py file, you'll find test cases for creating, updating, reading, and deleting both Invoice and InvoiceDetail objects. These test cases print informative messages before and after each operation to help you understand the test execution.



