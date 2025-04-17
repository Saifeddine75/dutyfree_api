import random
from datetime import datetime, timedelta

import requests
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Generate random customer and purchase data, and POST to API."

    def add_arguments(self, parser):
        parser.add_argument(
            "--api-version", type=str, default="v1", help="API version (default: v1)"
        )
        parser.add_argument(
            "--count",
            type=int,
            default=5,
            help="Number of customers to generate (default: 5)",
        )

    def handle(self, **options):
        count = options["count"]
        api_version = options["api_version"]
        url = f"http://127.0.0.1:8000/{api_version}/customers/"

        self.stdout.write(f"Generating {count} fake customers with purchases...")

        customers = [self.generate_customer() for _ in range(count)]

        self.stdout.write(f"Sending data to {url}...")
        response = requests.post(url, json=customers)

        if 200 <= response.status_code < 300:
            self.stdout.write(f"Success! Response: {response.status_code}")
        else:
            self.stderr.write(
                f"Failed with status {response.status_code}:\n{response.text}"
            )

    def generate_customer(self):
        customers = {
            "salutation": random.choice(["1", "2"]),
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "postal_code": fake.postcode(),
            "city": fake.city(),
            "email": fake.email(),
            "purchases": [
                self.generate_purchase() for _ in range(random.randint(1, 3))
            ],
        }
        print("customers", customers)
        return customers

    def generate_purchase(self):
        return {
            "product_id": random.randint(1, 100),
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(5.0, 200.0), 2),
            "currency": random.choice(["EUR", "USD", "GBP", "JPY"]),
            "purchased_at": (
                datetime.today() - timedelta(days=random.randint(0, 365))
            ).strftime("%Y-%m-%d"),
        }
