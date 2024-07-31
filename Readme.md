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

- **Base URL**: `http://yourhostname.com/v1/`
- **Customer Endpoint**: `http://yourhostname.com/v1/customers/`
- **Customer Test Endpoint**: `http://127.0.0.1:8000/v1/customers/`

### **Get started**

#### 1) Create your folder project
`mkdir -p dutyfree/src/`

#### 2) Create et activate virtual env
`python3 -m venv .env`
`.env/Scripts/activate`

#### 3) Install dependancies
`pip install -r requirement.txt`

#### 4) Start local server
`python manage.py runserver`


## 2. CLI Commands

**Send Payload from CSV**

You can upload data from CSV files using the CLI. Use the following command to send customer and purchase data:
`python purchase_api_cli.py data/customers.csv data/purchases.csv "http://127.0.0.1:8000/v1/customers/"`

**Send payload from json**
- **Create your json payload**: `touch payload.json`
- **Excecute following script**: `./post_customer.sh`

## 3. Manage your database

**Scripts to manage your objects**

- **List all database objects**: `python dutyfree_api/list_all_objects.py`
- **Delete all database objects**: `python dutyfree_api/delete_all_objects.py`

## 4. Read your logs
- **Log path**: `dutyfree_api/debug.log`

## 5. Minor issues
- **Title outside payload provoke errors**
- **Fix date format for the field *purchased_at***
- **Fix hostname and routers**
