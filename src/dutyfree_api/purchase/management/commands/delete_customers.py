from django.core.management.base import BaseCommand
from purchase.models import Customers


class Command(BaseCommand):
    help = "Display all customers and purchases"

    def handle(self, *args, **kwargs):

        print("Deleting all customers...")
        customers_list = Customers.objects.all().delete()
        print(Customers.objects.all())

        self.stdout.write("📋 Customers deleted:")
        for customer in customers_list:
            self.stdout.write(str(customer))
