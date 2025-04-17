from django.core.management.base import BaseCommand
from purchase.models import Purchases


class Command(BaseCommand):
    help = "Display all customers and purchases"

    def handle(self, *args, **kwargs):

        print("Deleting all purchases...")
        purchases_list = Purchases.objects.all().delete()
        print(Purchases.objects.all())

        self.stdout.write("\n🛍️ Purchases:")
        for purchase in purchases_list:
            self.stdout.write(str(purchase))
