import robin_stocks.robinhood as rs
import os 
import sys

# Login to Robinhood account
robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username=robin_user,
         password=robin_pass,
         expiresIn=86400,
         by_sms=True)

# Get top 100 stocks from Robinhood
def get_tickers():
    tickers = rs.get_top_100()
    stocks = []
    for number in range(len(tickers)):
        for element in tickers[0]:
            if element == "symbol":
                stocks.append(tickers[number][element])
    return stocks

# Get user desired tickers from ticker_list
def get_tickers_stocks(file_name):
    with open(file_name, 'r') as read:
        user_stocks = read.readlines()
        for i in range(len(user_stocks)):
            user_stocks[i] = user_stocks[i].strip("\i")
        return user_stocks 

# Filter tickers by user desired price
def filter_ticker_by_price(stocks, price_to_filter):
    stocks_under_price = {}
    for stock in stocks:
        new_stocks = rs.get_quotes([stock])
        for new_stock in new_stocks:
            if float(new_stock["last_trade_price"]) <= price_to_filter:
                local_stock = new_stock["symbol"]
                stocks_under_price[local_stock] = new_stock["last_trade_price"]
    return stocks_under_price

list_or_pull = input("Do you want to get the top 100 from Robinhood or pull stocks from a file? (1 for Robinhood, 2 for pulling stocks from a file): ")

if list_or_pull == "1":
    top_stocks = get_tickers()
elif list_or_pull == "2":
    file_name = input("Enter the file name containing the stocks: ")
    top_stocks = get_tickers_stocks(file_name)
else:
    print("Invalid choice.")
    sys.exit(1)

expiration_date = input("Enter an expiration date for the option contract (YYYY-MM-DD format): ")
calls_or_puts = input("Enter 1 for calls or 2 for puts: ")
strike_price = float(input("Enter the desired strike price: "))

# Find high probability trades for option premium
high_probability_trades = []
for stock in top_stocks:
    option_quotes = rs.find_options_by_expiration_and_strike(stock, expiration_date, strike_price)
    if calls_or_puts == "1":
        # Filter for calls
        calls = [quote for quote in option_quotes if quote['type'] == 'call']
        for call in calls:
            if call['premium'] > 0.5:  # Adjust premium threshold as desired
                high_probability_trades.append({
                    'stock': stock,
                    'option_type': 'Call',
                    'expiration_date': expiration_date,
                    'strike_price': call['strike_price'],
                    'premium': call['premium']
                })
    elif calls_or_puts == "2":
        # Filter for puts
        puts = [quote for quote in option_quotes if quote['type'] == 'put']
        for put in puts:
            if put['premium'] > 0.5:  # Adjust premium threshold as desired
                high_probability_trades.append({
                    'stock': stock,
                    'option_type': 'Put',
                    'expiration_date': expiration_date,
                    'strike_price': put['strike_price'],
                    'premium': put['premium']
                })

# Print high probability trades
for trade in high_probability_trades:
    print(trade)