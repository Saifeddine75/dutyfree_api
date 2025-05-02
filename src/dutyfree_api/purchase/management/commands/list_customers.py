from django.core.management.base import BaseCommand
from purchase.models import Customers


class Command(BaseCommand):
    help = "Display all customers"

    def handle(self, *args, **kwargs):
        customers_list = Customers.objects.all()

        self.stdout.write("📋 Customers:")
        for customer in customers_list:
            self.stdout.write(str(customer))
