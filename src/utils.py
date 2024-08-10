from json import dumps, dump, loads
from requests import post
from csv import DictReader

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
    