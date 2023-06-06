import robin_stocks.robinhood as rs
import os 

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username=robin_user,
         password=robin_pass,
         expiresIn=86400,
         by_sms=True)


def get_tickers():
    tickers = rs.get_top_100()
    stocks = []
    for number in range(len(tickers)):
        for element in tickers[0]:
            if element == "symbol":
                tickers.append(tickers[number][element])
    return stocks

def get_tickers_stocks(file_name):
    with open(file_name, 'r') as read:
        user_stocks = read.readlines()
        for i in (len(user_stocks)):
            user_stocks[i] = user_stocks[i].strip("\i")
        return user_stocks 

def filter_ticker_by_price(stocks):
    stocks_under_price = {}
    for stock in stocks:
        new_stocks = rs.get_quotes(stocks)
        for new_stock in new_stocks:
            if float(new_stock["last_trade_price"]) <= price_to_filter:
                local_stock = new_stock["symbol"]
                stocks_under_price[local_stock] = new_stock["last_trade_price"]
    print(stocks_under_price)
    return stocks_under_price 



