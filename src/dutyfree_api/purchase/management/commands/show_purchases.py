from django.core.management.base import BaseCommand
from purchase.models import Purchases

class Command(BaseCommand):
    help = "Display all purchases"

    def handle(self, *args, **kwargs):
        purchases_list = Purchases.objects.all()

        self.stdout.write("📋 Purchases:")
        for purchase in purchases_list:
            self.stdout.write(str(purchase))
