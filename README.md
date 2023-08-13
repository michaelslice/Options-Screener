# Options-Screener
A program that leverages the Robinhood API to fetch options contract data, allowing users to filter and analyze stocks based on specific criteria, and calculate metrics such as percent win and probability of losing. 

## Prerequisites 

For this program to work you must have a verified options account from Robinhood.

## Initialization 

When the program is initially run, the user will be prompted to enter their Robinhood username and password. Your username will be the email linked to your account. 

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/e75c0963-3379-4665-b433-9557dc854e3b)

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/38b2feca-7d0a-450a-9b76-07b3a9d3c399)

When you type in your Robinhood password, the characters will not show for your safety.

## Searching

After typing in your username and password you will be asked if you want to search options from Robinhood's top 100 tickers or search for tickers from a file.

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/ffdfcfcd-c716-4555-8b47-0a1878303fd5)

## Expiration Date

After deciding where to pull tickers from, you will be prompted for a desired expiration date for the options contract. You must enter a valid expiration date, if you are not sure check the Robinhood website. 

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/f2be824b-9466-496e-a6af-af2384f92ca1)

## Calls or Puts

After deciding the option expiration date, you will be asked if you want to look at call or put contracts.

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/3d77174f-2889-49ac-88ed-246b8347710e)

## Strike Price

After deciding on calls or puts, you will be asked for the desired strike price.

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/5809e846-f475-44b4-bbab-eb5749ed74e1)

## File Name

If you press 2 you will be prompted for the file name to search in. 

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/519a1e9a-be79-44a0-b66d-f9641c075ef4)

## Loading Data

After typing in the file name, the call to the Robinhood API will be made

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/d1b1d26c-29cf-410d-a344-34cecf45e702)

## Final

In the terminal, a large list of option contracts will appear, with data for cash required to cover, strike price, option contract price per share, current stock price, percent win, and probability of losing.

![image](https://github.com/michaelslice/Options-Screener/assets/110714088/e551a05c-ccbb-40e2-803f-905c7f8ff108)



