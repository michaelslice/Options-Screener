import robin_stocks.robinhood as rs
import os
import sys
import re


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
            user_stocks[i] = user_stocks[i].strip("\n")
        return user_stocks

def filter_ticker_by_price(stocks, price_to_filter):
    stocks_under_price = {}
    for stock in stocks:
        new_stocks = rs.get_quotes([stock])
        for new_stock in new_stocks:
            last_trade_price = new_stock["last_trade_price"]
            print("Last trade price for", stock, ":", last_trade_price)  # Debug print

            try:
                # Convert the last_trade_price to float
                last_trade_price = float(last_trade_price)
            except ValueError:
                
                continue

            if last_trade_price <= price_to_filter:
                local_stock = new_stock["symbol"]
                stocks_under_price[local_stock] = last_trade_price
    return stocks_under_price

def calculate_percent_win(option_price, cash_required):

    print("Before conversion - option_price:", option_price, "cash_required:", cash_required)
    option_price = float(option_price)
    cash_required = float(cash_required)

    # Check if cash_required is zero to avoid division by zero
    if cash_required == 0:
        # Assign a default value (e.g., 1) to avoid division by zero
        cash_required = 1

    percent_win = (option_price / cash_required) * 100
    return percent_win

# Function to calculate probability of losing
def calculate_probability_lose(delta):
    probability_lose = delta * 100
    return probability_lose

list_or_pull = input("Do you want to get the top 100 from Robinhood or pull stocks from a file? (1 for Robinhood, 2 for pulling stocks from a file): ")

expiration_date = input("Enter an expiration date for the option contract (YYYY-MM-DD format): ")
calls_or_puts = input("Enter 1 for calls or 2 for puts: ")
strike_price = float(input("Enter the desired strike price: "))

if list_or_pull == "1":
    tickers = get_tickers()
elif list_or_pull == "2":
    file_name = input("Enter the file name containing the desired stocks: ")
    tickers = get_tickers_stocks(file_name)
else:
    sys.exit("Invalid choice. Exiting...")

for ticker in tickers:
    if calls_or_puts == "1":
        option_type = "call"
    elif calls_or_puts == "2":
        option_type = "put"
    else:
        sys.exit("Invalid choice. Exiting...")
    
    options = rs.find_options_by_expiration(ticker, expirationDate=expiration_date, optionType=option_type)
    
for option in options:
    option_symbol = option['symbol']
    option_price = option['last_trade_price']
    option_strike_price = option['strike_price']
    option_contract_price_per_share = option['ask_price']
    stock_price = rs.stocks.get_latest_price(ticker, includeExtendedHours=False)[0]

    if option_price is None or option_strike_price is None or option['delta'] is None:
        # Skip this option as 'last_trade_price', 'strike_price', or 'delta' is missing
        continue

    # Convert to float
    option_price = float(option_price)
    option_strike_price = float(option_strike_price)
    delta = float(option['delta'])

    # Calculate cash required for 100 shares or securing a put
    if option_type == "call":
        cash_required = option_strike_price * 100
    else:
        cash_required = option_price * 100

    # Calculate percent win
    percent_win = calculate_percent_win(option_price, cash_required)

    # Calculate probability of losing
    probability_lose = calculate_probability_lose(delta)

    # Print the information
    print("Option Symbol:", option_symbol)
    print("Strike Price:", option_strike_price)
    print("Option Contract Price per Share:", option_contract_price_per_share)
    print("Stock Price:", stock_price)
    print("Percent Win:", percent_win)
    print("Probability of Losing:", probability_lose)
    print("------------------------")