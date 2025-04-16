from django.core.management.base import BaseCommand
from purchase.models import Customers, Purchases

class Command(BaseCommand):
    help = "Display all customers and purchases"

    def handle(self, *args, **kwargs):
        customers_list = Customers.objects.all()
        purchases_list = Purchases.objects.all()

        self.stdout.write("📋 Customers:")
        for customer in customers_list:
            self.stdout.write(str(customer))

        self.stdout.write("\n🛍️ Purchases:")
        for purchase in purchases_list:
            self.stdout.write(str(purchase))