
import yfinance as yf

userrequest = input("Do you need help finding the price of a stock? ")

while userrequest == "yes":
    stockticker = input("Ticker of the stock price you want: ")

    stock2 = yf.Ticker(stockticker)

    stock2.info

userrequest = input(
    "Do you need further help finding the price of a stock? ")

print("See you around !")

# gotta chek the yf.Ticker thing, not pulling stock prices
