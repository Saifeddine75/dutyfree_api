# Customer & Purchases API

Welcome to the Customer & Purchases API documentation. This API is built using Django REST Framework (DRF) and allows for managing customer and purchase data effectively.

## 1. Overview

The Customer & Purchases API is designed to manage customer and purchase data. It provides endpoints to create and list customers and handle their purchases.

### **Models**

- **Customer**: Represents a customer in the system.
- **Purchase**: Represents a purchase made by a customer.

### **Views**

- **CustomerCreateListViewSet**: Handles creating new customers and listing existing ones.

### **API Endpoints**

- **Base URL**: `https://yourhostname.com/v1/`
- **Customer Endpoint**: `https://yourhostname.com/v1/customers/`
- **Customer Test Endpoint**: `http://127.0.0.1:8000/v1/customers/`

_For our test we will use the Customer Test Endpoint but if we deploy the Customer Endpoint will be used_

### **Get started**

#### a. Open your folder project

`cd dutyfree_api/`

#### b. Create et activate virtual env

`python3 -m venv .venv`
`.env/Scripts/activate`

#### c. Install dependancies

`pip install -r requirement.txt`

#### d. Start local server

`cd src/dutyfree_api/`
`python manage.py runserver`

## 2. CLI Commands

**Send Payload from CSV**

You can upload data from CSV files using the CLI. Use the following command to send customer and purchase data:
`python purchase_api_cli data/customers.csv data/purchases.csv "http://127.0.0.1:8000/v1/customers/"`

**Send payload from json**

- **Create and or use the json payload provided in data folder:**: `data/payload.json`
- **Execute following script**: `./post_json_payload.sh`

## 3. Read your logs

- **Log path**: `dutyfree_api/debug.log`

## 4. Unit tests

`cd dutyfree_api/src/dutyfree_api`
`pytest tests`

## 5. Manage your database easily

**Scripts to manage your objects**

**Initialize Database**

- **Generate random customers purchases objects**: `python manage.py generate_purchases`

**List records**

- **List all database objects**: `python manage.py list_all`
- **List all customers objects**: `python manage.py list_customers`
- **List all purchases objects**: `python manage.py list_purchases`

**Delete records**
- **Delete all database objects**: `python manage.py delete_all`
- **Delete all customers objects**: `python manage.py delete_customers`
- **Delete all purchases objects**: `python manage.py delete_purchases`
