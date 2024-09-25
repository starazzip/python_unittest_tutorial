# src/calculator.py
import requests
class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a / b

    def get_exchange_rate(self, currency):
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{currency}')
        data = response.json()
        return data['rates']['USD']
    
if __name__=="__main__":
    c = Calculator()
    rate = c.get_exchange_rate('EUR')
    pass