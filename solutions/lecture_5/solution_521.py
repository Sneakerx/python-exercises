"""
The user shall input a cryptocurrency symbol (e.g., BTC, ETH, LTC)
and a fiat currency symbol (e.g., USD, EUR, GBP).
The program should then fetch and display the current price
of the specified cryptocurrency in the specified fiat currency

Example: Request BTC in EURO:
https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-EUR
"""

import requests
from datetime import datetime

url = "https://api.kucoin.com/api/v1/market/orderbook/level1"

coin = input("Geben Sie einen Coin ein ").upper()
fiat = input("Geben Sie eine Währung ein ").upper()

result = requests.get(url, params={"symbol": f"{coin}-{fiat}"})
data = result.json()
price = float(data["data"]["price"])
timestampSec = data["data"]["time"] / 1000.0

formattedTime = datetime.fromtimestamp(timestampSec).strftime("%Y-%m-%d %H:%M:%S")

print(f"{formattedTime}: Der Wert von {coin} beträgt: {price:.2f} {fiat}")
