# code an investment trading bot that trades using fake paper money
import robin_stocks as r
import pandas as pd
import time

login = r.login(username, password)

r.build_holdings()
r.profiles.load_basic_profile()

# def visualize_price(ticker_list, span = "year", bounds = "regular"):   
#     for t in range(len(ticker_list)):
#         name = str(rh.get_name_by_symbol(ticker_list[t]))
#         hist = rh.stocks.get_stock_historicals(ticker_list[t], span=span, bounds=bounds)
#         hist_df = pd.DataFrame()
#         for i in range(len(hist)):
#             df = pd.DataFrame(hist[i], index = [i])
#             hist_df = pd.concat([hist_df,df])
#         hist_df.begins_at = pd.to_datetime(hist_df.begins_at, infer_datetime_format=True)
#         hist_df.open_price = hist_df.open_price.astype("float32")
#         hist_df.close_price = hist_df.close_price.astype("float32")
#         hist_df.high_price = hist_df.high_price.astype("float32")
#         hist_df.low_price = hist_df.low_price.astype("float32")

#         ax = hist_df.plot(x = "begins_at", y = "open_price", figsize = (16,8))
#         ax.fill_between(hist_df.begins_at, hist_df.low_price, hist_df.high_price, alpha = 0.5)
#         ax.set_xlabel("Date")
#         ax.set_ylabel("Price (USD)")
#         ax.legend([ticker_list[t]])
#         ax.set_title(name)
#     return

def extract_list():
    ticker_list = list(r.build_holdings().keys())
    return ticker_list

ticker_list = extract_list()
# visualize_price(ticker_list, span = "year", bounds = "regular")

def trading_bot(trading_dict):
    holdings = r.build_holdings()
    holdings_df = pd.DataFrame()
    for i in range(len(holdings)):
        ticker = list(holdings.items())[i][0]
        holding_df = pd.DataFrame(list(holdings.items())[i][1], index = [i])
        holding_df["ticker"] = ticker
        holdings_df = pd.concat([holdings_df, holding_df])
    holdings_df = holdings_df[["ticker", "price", "quantity", "percent_change","average_buy_price", "equity", "equity_change","pe_ratio", "type", "name", "id" ]]

    for j in range(len(trading_dict)):
        holding_df = holdings_df[holdings_df.ticker == list(trading_dict.keys())[j]]
        if holding_df["percent_change"].astype("float32")[0] <= list(trading_dict.values())[j][0]:
            buy_string = "Buying " + str(holding_df["ticker"][0]) + " at " + time.ctime()
            print(buy_string)
            r.orders.order_buy_market(holding_df["ticker"][0],1,timeInForce= "gfd")
        else:
            print("Nothing to buy")

        if holding_df["percent_change"].astype("float32")[0] >= list(trading_dict.values())[j][1]:
            sell_string = "Buying " + str(holding_df["ticker"][0]) + " at " + time.ctime()
            print(sell_string)
            r.orders.order_sell_market(holding_df["ticker"][0],1,timeInForce= "gfd")
        else:
            print("Nothing to sell")

