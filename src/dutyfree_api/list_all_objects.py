
import os
import django
from django.conf import settings

def setup_django_environment():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dutyfree_api.settings')
    django.setup()

def run_shell_commands():
    from purchase.models import Customers, Purchases
    customers_list = Customers.objects.all()
    purchases_list = Purchases.objects.all()
    print("Customers:", customers_list.values())
    print("Purchases:", purchases_list.values())
        
if __name__ == "__main__":
    setup_django_environment()
    run_shell_commands()