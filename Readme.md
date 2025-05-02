# 📦 Customer & Purchases API

Welcome to the **Customer & Purchases API**, a Django REST Framework-based application for managing customers and their purchase records.

---

## 🚀 Overview

This API provides endpoints for:

- Creating and listing **customers**
- Submitting and retrieving **purchase** data

### 🧩 Models

- **Customer**: Represents a client in the system  
- **Purchase**: Represents a transaction made by a customer

### 📡 Views

- `CustomerCreateListViewSet`: Handles customer creation and listing

---

## 🔗 API Endpoints

| Endpoint Type        | URL |
|----------------------|-----|
| **Base URL**         | `https://yourhostname.com/v1/` |
| **Production (Customer)** | `https://yourhostname.com/v1/customers/` |
| **Local (Customer)** | `http://127.0.0.1:8000/v1/customers/` |

For testing locally, use the local endpoint.

---

## ⚙️ Getting Started

1. **Navigate to project directory**
   ```bash
   cd dutyfree_api/
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or .env/Scripts/activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server**
   ```bash
   cd src/dutyfree_api/
   python manage.py runserver
   ```

---

## 🛠 CLI Usage

### ✅ Upload Data from CSV

```bash
python purchase_api_cli data/customers.csv data/purchases.csv "http://127.0.0.1:8000/v1/customers/"
```

### ✅ Send Payload from JSON

1. Edit or use the existing file: `data/payload.json`
2. Execute:
   ```bash
   ./post_json_payload.sh
   ```

---

## 📜 Logs

All logs are saved in:
```
dutyfree_api/debug.log
```

---

## 🧪 Running Tests

Run unit tests using `pytest`:
```bash
cd dutyfree_api/src/dutyfree_api/
pytest tests
```

---

## 🗃 Database Management Scripts

### 🔄 Initialize with Fake Data
```bash
python manage.py generate_purchases
```

### 📋 List Records

- All records: `python manage.py list_all`
- Customers: `python manage.py list_customers`
- Purchases: `python manage.py list_purchases`

### ❌ Delete Records

- All records: `python manage.py delete_all`
- Customers: `python manage.py delete_customers`
- Purchases: `python manage.py delete_purchases`
