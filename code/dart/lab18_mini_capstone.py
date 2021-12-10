# code an investment trading bot that trades using fake paper money
import alpaca_trade_api as tradeapi
import numpy as np
import time

url = "https://paper-api.alpaca.markets" # url used to access website

sec_key = "hAoJ9HSwKWvQ7wBjMcRwoT7yTxdDm2VfMyJPG0vW"

pub_key = "AK11YJE0ZV9IEZ1AUK9Q"

api = tradeapi.REST(key_id=pub_key, secret_key=sec_key, base_url=url)

# purchase a stock
api.submit_order(
    symbol = "TSLA",
    qty = 1,
    side = "buy",
    type = "market",
    time_in_force = "gtc",
)

# sell a stock
api.submit_order(
    symbol = "TSLA",
    qty = 1,
    side = "sell",
    type = "market",
    time_in_force = "gtc",
)

symbol = "TSLA"

while True:
    print("")
    print("Checking Price...")

    market_data = api.get_barset(symbol, "minute", limit = 10)

    close_list = []