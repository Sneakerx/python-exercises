"""
The user shall input a cryptocurrency symbol (e.g., BTC, ETH, LTC)
and a fiat currency symbol (e.g., USD, EUR, GBP).
The program should then fetch and display the current price
of the specified cryptocurrency in the specified fiat currency.
Add exception handling to manage potential errors during the API request.
Add printing of full names of the cryptocurrencies and fiat currencies.

Example: Request BTC in EURO:
https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-EUR

Example: Request BTC full name
https://api.kucoin.com/api/v3/currencies/BTC
"""

import requests
from datetime import datetime

url = "https://api.kucoin.com/api/"
tag_price = "v1/market/orderbook/level1"
tag_names = "v3/currencies"

coin = input("Geben Sie einen Coin ein ").upper()
fiat = input("Geben Sie eine Währung ein ").upper()


def get_price():
    try:
        result = requests.get(f"{url}{tag_price}", params={"symbol": f"{coin}-{fiat}"})
        data = result.json()
        price = data["data"]["price"]
        time_sec = data["data"]["time"] / 1000.0
        time_string = datetime.fromtimestamp(time_sec).strftime("%Y-%m-%d %H:%M:%S")
    except requests.exceptions.RequestException as e:
        print(f"Ein Fehler mit der API ist aufgetreten: {e}")
        return False
    except KeyError:
        print("Preis objekt ist nicht verfügbar oder wurde verschoben.")
        return False
    except TypeError:
        print(f"Der Coin oder die Währung sind falsch: {coin}, {fiat}")
        return False
    else:
        return price, time_string


def print_price(price, time_string):
    try:
        coin_name = requests.get(f"{url}{tag_names}/{coin}").json()["data"]["fullName"]
        fiat_name = requests.get(f"{url}{tag_names}/{fiat}").json()["data"]["fullName"]
    except requests.exceptions.RequestException as e:
        print(f"Ein Fehler mit der API ist aufgetreten: {e}")
        return False
    except KeyError:
        print("Preis objekt ist nicht verfügbar oder wurde verschoben.")
        return False
    else:
        print(f"{time_string}: Der Wert von {coin_name} beträgt: {price} {fiat_name}")


price, time_string = get_price()
if price:
    print_price(price, time_string)
