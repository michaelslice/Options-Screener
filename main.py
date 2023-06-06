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

def get_user_stocks(ticker_list):
    with open("ticker_list", 'r') as read:
        user_stocks = read.readlines()
        for i in (len(user_stocks)):
            user_stocks[i] = user_stocks[i].strip("\i")
        return user_stocks 










