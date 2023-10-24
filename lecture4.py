# Python Example: Creating a Simple Time Series
dates = ["1st January", "2nd January", "3rd January"]
stock_prices = [150, 152, 151]
for date, price in zip(dates, stock_prices):
    print(f"{date} : ${price}")

#2 Python Exercises for Financial Time Series
#Exercice 1 avec solution
dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]

def calculate_average(prices):
    return sum(prices) / len(prices)

average_price = calculate_average(stock_prices)
print(f"Average Stock Price: ${average_price}")

#Exercice 2 
def max(dates, stock_prices):
    max_prices = stock_prices[0]
    max_day = dates[0]
    for i in range(1, len(stock_prices)):
     if stock_prices[i] > max_prices:
        max_prices = stock_prices[i]
        max_day = dates[i]
    return max_day

Jourmax = max(dates, stock_prices)
print(Jourmax)

#Exercice 3 


def trend(dates, stock_prices):
   bull = 0
   bear = 0
   stable = 0
   for i in range(1, len(stock_prices)):
      if stock_prices[i] > stock_prices [i-1]:
         bull += 1
      elif stock_prices[i] < stock_prices[i-1]:
         bear += 1
      else:
         stable += 1
         
         
        return bull, bear, stable   #JARRIVE PAS A LALIGNER AVEC "FOR"

dates = ["4th January", "5th January", "6th January","7th January", "8th January"]
stock_prices = [155, 156, 153, 157, 152]

bullish, bearish, stable = trend(dates, stock_prices)
print(max(bullish, bearish, stable))

#MARCHE PAAAAAAAAAS





#2.2 Exercises related to ”Importance of Time Series in Finance”

#Exercice 1 avec solution 
import statistics

def calculate_volatility(prices):
    return statistics.stdev(prices)

volatility = calculate_volatility(stock_prices)
print(f"Volatility: ${volatility}")

#Exercice 2 
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
stock_prices = [150, 152, 151, 153, 152]

def average(stock_prices):
   average = sum(stock_prices) / len(stock_prices)
   return average 

avg = average(stock_prices)

for i in range (1, len(stock_prices)):
   if stock_prices[i] > avg : 
      print(dates[i], "est au dessus de la moyenne")


#Exercice 3 a l'aide de ChatGPT
def forecast_next_day_price(stock_prices):
    if len(stock_prices) < 2:
        return None  # Not enough data to make a forecast

    # Calculate the daily changes (difference between consecutive days)
    daily_changes = [stock_prices[i] - stock_prices[i-1] for i in range(1, len(stock_prices))]

    # Calculate the average daily change
    average_change = sum(daily_changes) / len(daily_changes)

    # Forecast the next day's stock price
    last_known_price = stock_prices[-1]
    forecasted_price = last_known_price + average_change

    return forecasted_price

# Example data
stock_prices = [100, 102, 104, 103, 105]

# Forecast the next day's stock price
forecasted_price = forecast_next_day_price(stock_prices)

if forecasted_price is not None:
    print(f"Forecasted Next Day's Stock Price: {forecasted_price}")
else:
    print("Insufficient data for forecasting.")







#3 Time Value of Money
#3.1.1 Present Value (PV)
# Python Example: Calculating Present Value
def present_value(fv, r, n):
    return fv / (1 + r)**n

# Given values
FV = 110
r = 0.1
n = 1

PV = present_value(FV, r, n)
print(f"The present value is: ${PV:.2f}")



#3.1.2 Future Value (FV)
# Python Example: Calculating Future Value
def future_value(pv, r, n):
    return pv * (1 + r)**n

# Given values
PV = 100
r = 0.1
n = 1

FV = future_value(PV, r, n)
print(f"The future value is: ${FV:.2f}")

#3.1.3 Discounting and Compounding
# Python Example: Compounding
def compound(pv, r):
    return pv * (1 + r)

# Given values
PV = 100
r = 0.1

FV = compound(PV, r)
print(f"After one year with a 10% interest rate, you'll have: ${FV:.2f}")

# Python Example: Discounting
def discount(fv, r):
    return fv / (1 + r)

# Given values
FV = 110
r = 0.1

PV = discount(FV, r)
print(f"The present value of $110 after one year with a 10% interest rate is: ${PV:.2f}")




#4 Python Exercises for Time Value of Money
#4.1 Exercises related to ”Present Value (PV)”
#Exercice 1 with solution
def present_value(fv, r, n):
    return fv / (1 + r)**n

FV = 120
r = 0.05
n = 2

PV = present_value(FV, r, n)
print(f"The present value is: ${PV:.2f}")

#Exercice 2 
def present_value(fv, r, n):
   return fv / (1 + r)**n

FV = 500
r = 0.06 
n = 2

PV = present_value(FV, r, n)
print(f"The present value is : ${PV:.2f}")


#Exercice 3 
#Same than Exercice 2 but FV = 5000, r = 0.04, n = 5



#4.2 Exercises related to ”Future Value (FV)”
#Exercice 1 with solution 
def future_value(pv, r, n):
    return pv * (1 + r)**n

PV = 90
r = 0.07
n = 1

FV = future_value(PV, r, n)
print(f"The future value is: ${FV:.2f}")

#Exercice 2
def future_value(pv, r, n):
    return pv * (1 + r)**n

PV = 200
r = 0.03
n = 2

FV = future_value(PV, r, n)
print(f"The future value is: ${FV:.2f}")

#Exercice 3
# Same than Exercice 2 but FV = 150, r = 0.05, n = 3



#4.3 Exercises related to ”Discounting and Compounding”
#Exercise 1 (With Solution):
def compound(pv, r):
    return pv * (1 + r)

PV = 80
r = 0.09

FV = compound(PV, r)
print(f"After one year with a 9% interest rate, you'll have: ${FV:.2f}")

#Exercice 2 
def compound(pv, r):
    return pv * (1 + r)

PV = 115
r = 0.08

FV = compound(PV, r)
print(f"After one year with a 9% interest rate, you'll have: ${FV:.2f}")

#Exercice 3 
def present_value(fv, r, n):
   return fv / (1 + r)**n

FV = 500
r = 0.06 
n = 2

PV = present_value(FV, r, n)
print(f"You need to invest: ${PV:.2f} to reach ${FV:.2f}")

#Exercice 4 
def present_value(fv, r, n):
   return fv / (1 + r)**n

FV = 180
r = 0.1 
n = 2

PV = present_value(FV, r, n)
print(f"You need to invest: ${PV:.2f} today to reach ${FV:.2f} in {n} years")


#Exercice 5
def present_value(fv, r, n):
   return fv / (1 + r)**n

FV = 1000
r = 0.07
n = 3

PV = present_value(FV, r, n)
print(f"You need to invest: ${PV:.2f} today to reach ${FV:.2f} in {n} years")



#4.4 Working with Time Series Data using pandas
import yfinance as yf

# Download Apple stock data
apple_data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")

# Display the first few rows of the data
print(apple_data.head())

#4.4.3 Working with Time Series Data
import matplotlib.pyplot as plt

apple_data['Close'].plot(figsize=(10, 5))
plt.title('Apple Stock Closing Prices')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Moving average adding
apple_data['50-day MA'] = apple_data['Close'].rolling(window=50).mean()
apple_data[['Close', '50-day MA']].plot(figsize=(10, 5))
plt.title('Apple Stock Prices with 50-day Moving Average')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Timeframe change
weekly_data = apple_data['Close'].resample('W').mean()
weekly_data.plot(figsize=(10, 5))
plt.title('Apple Stock Weekly Closing Prices')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()


#4.5 Python Exercises for Working with Time Series Data using pandas
#4.5.1 Exercises related to ”Fetching Data from Yahoo Finance”
#Exercice 1 with solution

# Download Microsoft stock data
msft_data = yf.download("MSFT", start="2021-01-01", end="2022-01-01")
print(msft_data.head())


#Exercice 2 
google_data = yf.download("GOOGL", start="2021-01-01", end="2022-01-01")
print(google_data.head())

#Exercice 3 
amzn_data = yf.download("AMZN", start="2021-10-01", end="2021-12-31")
print(amzn_data.head())


#4.5.2 Exercises related to ”Plotting the closing prices”
#Exercice 1 with solution 
tesla_data = yf.download("TSLA", start="2020-01-01", end="2021-01-01")
tesla_data['Close'].plot(figsize=(10, 5))
plt.title('Tesla Stock Closing Prices 2020')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 2 
netflix_data = yf.download("NFLX", start="2022-01-01", end="2022-03-31")
netflix_data['Close'].plot(figsize=(10, 5))
plt.title('Netflix Stock Closing Prices Q1 2022')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 3 
facebook_data = yf.download("META", start="2019-01-01", end="2019-12-30")
facebook_data['Close'].plot(figsize=(10, 5))
plt.title('Netflix Stock Closing Prices Q1 2022')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#4.5.3 Exercises related to ”Calculating moving averages”
ibm_data = yf.download("IBM", start="2020-01-01", end="2021-01-01")
ibm_data['30-day MA'] = ibm_data['Close'].rolling(window=30).mean()
ibm_data[['Close', '30-day MA']].plot(figsize=(10, 5))
plt.title('IBM Stock Prices with 30-day Moving Average 2020')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 2 
adobe_data = yf.download("ADBE", start="2021-01-01", end="2021-12-30")
adobe_data['20-day MA'] = adobe_data['Close'].rolling(window=20).mean()
adobe_data[['Close', '20-day MA']].plot(figsize=(10, 5))
plt.title('Adobe Stock Prices with 20-day Moving Average 2021')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 3
nvidia_data = yf.download("IBM", start="2022-01-01", end="2022-12-30")
nvidia_data['40-day MA'] = nvidia_data['Close'].rolling(window=40).mean()
nvidia_data[['Close', '40-day MA']].plot(figsize=(10, 5))
plt.title('Nvidia Stock Prices with 40-day Moving Average 2022')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()


#4.5.4 Exercises related to ”Resampling”
#Exercice 1 with solution 
sbux_data = yf.download("SBUX", start="2020-01-01", end="2021-01-01")
monthly_data = sbux_data['Close'].resample('M').mean()
monthly_data.plot(figsize=(10, 5))
plt.title('Starbucks Monthly Average Closing Prices 2020')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 2 
Disney_data = yf.download("DIS", start="2019-01-01", end="2020-01-01")
biweekly_data = Disney_data['Close'].resample('2W').mean()  #doesn't work it put weekly
biweekly_data.plot(figsize=(10, 5))
plt.title('Disney biweekly Average Closing Prices 2019')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

#Exercice 3 
Coca_data = yf.download("DIS", start="2020-01-01", end="2021-01-01")
quaterly_data = Coca_data['Close'].resample('Q').mean()  
quaterly_data.plot(figsize=(10, 5))
plt.title('Coca quaterly Average Closing Prices 2020')
plt.ylabel('Price (in \$)')
plt.xlabel('Date')
plt.show()

