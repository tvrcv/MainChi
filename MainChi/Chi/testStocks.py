
import yfinance as yf

userrequest = input("Do you need help finding the price of a stock? ")

while userrequest == "Yes":
    stockticker = input("Ticker of the stock price you want: ")
    stock = yf.Ticker(stockticker)
    price = stock.info['regularMarketPrice']
    print(price)
    
    userrequest = input("Do you need further help finding the price of a stock? ") 

print("See you around !")





 



 
 

