
import os
import django
from django.conf import settings

def setup_django_environment():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dutyfree_api.settings')
    django.setup()

def run_shell_commands():
    from purchase.models import Customers, Purchases

    print("Deleting all customers...")
    Customers.objects.all().delete()
    print(Customers.objects.all())
    print("Deleting all purchases...")
    Purchases.objects.all().delete()
    print(Purchases.objects.all())
    
if __name__ == "__main__":
    setup_django_environment()
    run_shell_commands()