from datetime import datetime
from json import dumps, dump, loads
from requests import post
from csv import DictReader
from typing import Optional, Union


def check_data(payload):
    try:
        loads(dumps(payload))
    except ValueError as e:
        return False
    return True

def post_customers(url, data):
    headers = {
        'Content-Type': 'application/json'
    }
    with open('customer_payload.csv', mode='w', newline='', encoding='utf-8') as file:
        dump(data, file, indent=4)   
    response = post(url, headers=headers, data=dumps(data))
    print(response.status_code, response.text)
    return response

def get_csv_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = DictReader(file, delimiter=';')
        json_data = []
        for row in reader:
            json_data.append(row)
        return json_data

def create_customer_input(customers_data:list, customers:dict = {}, salutations:dict = {1: 'Mrs', 2: 'Mr'}) -> dict:
    """Create a dict with list of json customer data

    Args:
        customers_data (list): Customers instance customer details
        customers (dict, optional): Container to fill with input data. Defaults to {}.
        customer_id (None | int | list, optional): Customer to fill with input data. Defaults to None.
        salutations (dict, optional): Salutation of the customer. Defaults to {1: 'Mrs', 2: 'Mr'}.

    Returns:
        Dictionary filled with customer data: 
    """
    for customer in customers_data:
        customer_id = customer.get('customer_id')
        if customer_id:
            customers[customer_id]={
                'salutation': salutations[int(customer.get('title'))],
                'lastname': customer.get('lastname'),
                'firstname': customer.get('firstname'),
                'postal_code': customer.get('postal_code'),
                'city': customer.get('city'),
                'email': customer.get('email'),
                'purchases': []
            }
    return customers


def customer_attach_purchases(customers: dict, purchase_data: dict,  customer_id: Optional[Union[int, list]] = None):
    """Fill purchases customer column with input data

    Args:
        customers (dict): Container to fill with purchase details
        purchase_data (dict): Input data to fill customer with
        customer_id (None | int | list, optional): _description_. Defaults to None.
    """
    for purchase in purchase_data:
        customer_id = purchase.get('customer_id', customer_id)
        if customer_id in customers:
            customers[customer_id]['purchases'].append({
                # 'purchase_identifier': purchase.get('purchase_identifier'),
                'product_id': purchase.get('product_id'),
                'quantity': int(purchase.get('quantity')),
                'price': float(purchase.get('price')),
                'currency': purchase.get('currency'),
                'purchased_at': str(datetime.strptime(purchase.get('date'), '%Y-%m-%d').date())
            })