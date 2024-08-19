import requests

class CurrencyConverter:
  def __init__(self, api_key):
      self.apy_key = api_key
      self.url = f"https://v6.exchangerate-api.com/v6/e1a550cecb55207073a8da87/latest"

  def get_exchange_rate(self, from_currency, to_currency):
      response = requests.get(self.url + from_currency)
      data = response.json()
      if response.status_code == 200:
          rates = data['conversion_rates']
          return rates.get(to_currency, None)
      else:
          print(f"Error: {data['error-type']}")
          return None