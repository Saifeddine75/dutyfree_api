import pytest
from django.urls import reverse
from purchase.models import Customers
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db  # This marks all tests in the file as using the DB


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def customer_payload():
    return [
        {
            "salutation": "Mr.",
            "lastname": "Marc",
            "firstname": "Johnson",
            "email": "marc.johnson@example.com",
            "purchases": [
                {
                    "product_id": "75",
                    "price": 10,
                    "currency": "dollars",
                    "quantity": 1,
                    "purchased_at": "2023-01-01",
                },
                {
                    "product_id": "144",
                    "price": 20,
                    "currency": "dollars",
                    "quantity": 2,
                    "purchased_at": "2023-01-02",
                },
            ],
        },
        {
            "salutation": "Mrs.",
            "lastname": "Thomas",
            "firstname": "Muller",
            "email": "thomas.muller@example.com",
            "purchases": [
                {
                    "product_id": "541",
                    "price": 30,
                    "currency": "dollars",
                    "quantity": 3,
                    "purchased_at": "2023-01-03",
                }
            ],
        },
    ]


def test_list_customers_empty(api_client):
    response = api_client.get(reverse("customer-create-list"))
    assert response.status_code == 200
    assert response.json() == []


def test_create_multiple_customers(api_client, customer_payload):
    response = api_client.post(
        reverse("customer-create-list"), data=customer_payload, format="json"
    )

    assert response.status_code == 201
    assert len(response.data) == 2

    # Check if the customers were actually created in DB
    assert Customers.objects.count() == 2
    assert Customers.objects.filter(email="marc.johnson@example.com").exists()
    assert Customers.objects.filter(email="thomas.muller@example.com").exists()


def test_create_invalid_customer(api_client):
    bad_payload = [{"name": "", "email": "not-an-email"}]

    response = api_client.post(
        reverse("customer-create-list"), data=bad_payload, format="json"
    )

    assert response.status_code == 400
    assert "email" in str(response.data[0]) or "name" in str(response.data[0])
