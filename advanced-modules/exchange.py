import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

from_currency = input("Enter the currency you want to convert from: ").upper()
to_currency = input("Enter the currency you want to convert to: ").upper()
amount = float(input(f"Enter {from_currency} you want to convert: "))

response = requests.get(f"{api_url}{from_currency}")
response_json = response.json()
exchange_rate = response_json["conversion_rates"][to_currency]

converted_amount = amount * exchange_rate

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")