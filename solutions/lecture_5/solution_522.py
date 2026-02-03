"""
The user shall input a cryptocurrency symbol (e.g., BTC, ETH, LTC)
and a fiat currency symbol (e.g., USD, EUR, GBP).
The program should then fetch and display the current price
of the specified cryptocurrency in the specified fiat currency.
Add exception handling to manage potential errors during the API request.

Example: Request BTC in EURO:
https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-EUR
"""

import requests
from datetime import datetime

url = "https://api.kucoin.com/api/v1/market/orderbook/level1"

coin = input("Geben Sie einen Coin ein ").upper()
fiat = input("Geben Sie eine Währung ein ").upper()

try:
    result = requests.get(url, params={"symbol": f"{coin}-{fiat}"})
    data = result.json()
    price = data["data"]["price"]
    timestampSec = data["data"]["time"] / 1000.0
    formattedTime = datetime.fromtimestamp(timestampSec).strftime("%Y-%m-%d %H:%M:%S")
except requests.exceptions.RequestException as e:
    # RequestException: API ist down, kein Internet
    print(f"Ein Fehler mit der API ist aufgetreten: {e}")
except KeyError:
    # Key Error: API ändert sich: "data" oder "price" ist nicht mehr verfügbar
    print("Preisobjekt ist nicht verfügbar oder wurde verschoben.")
except TypeError:
    # Type Error: API gibt none zurück
    print(f"Der Coin oder die Währung sind falsch: {coin}, {fiat}")
else:
    print(f"{formattedTime}: Der Wert von {coin} beträgt: {price} {fiat}")
