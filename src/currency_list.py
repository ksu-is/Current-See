import os
dirname = os.path.dirname(__file__)
# https://stackoverflow.com/a/918178

CURRENCIES = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

CURRENCY_TO_ASSET = {
    currency: os.path.join(dirname, f"{currency}.jpg") for currency in CURRENCIES
}