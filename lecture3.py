# Exercice 1 exemple
class Bond:
    def __init__(self, price, coupon_rate, maturity):
        self.par_value = price
        self.coupon_rate = coupon_rate
        self.maturity = maturity

    def current_yield(self, market_price):
        return (self.coupon_rate * self.par_value) / market_price


ten_year_note = Bond(1000, 0.025, 10)
yield_on_note = ten_year_note.current_yield(950)
print(yield_on_note)


# Exercice 1
class Stock:
    def __init__(self, stock_name, price, dividend):
        self.stock_name = stock_name
        self.current_price = price
        self.dividend = dividend

    def yield_dividend(self):
        return self.dividend / self.current_price


APPL = Stock("APPL", 1000, 10)
print(APPL.yield_dividend())


# Exercie 2 : Financial Instrument Portfolio
class Portfolio:
    def __init__(self):
        self.instruments = []
        self.instruments.append(Stock("AAPL", 50, 200))
        self.instruments.append(Bond(1000, 0.025, 10))

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def total_value(self):
        total = 0
        for instrument in self.instruments:
            if isinstance(instrument, Stock):
                total += instrument.current_price
            elif isinstance(instrument, Bond):
                total += instrument.par_value
            # Add other instrument types as needed
        return total


my_portfolio = Portfolio()

# Calculate the total value of the portfolio
portfolio_value = my_portfolio.total_value()
print("Portfolio Total Value: ${:.2f}".format(portfolio_value))


# Exercice 3 Tentative
class CurrencyConverter:
    def __init__(self, pair, rate):
        self.pair = pair
        self.rate = rate

    def convert(self, amount):
        return amount * self


# Exercice 3 solution ChatGPT
class CurrencyConverter:
    def __init__(self):
        # Initialize a dictionary to store conversion rates for currency pairs.
        self.rates = {}

    def add_rate(self, source_currency, target_currency, rate):
        # Add or update a conversion rate for a currency pair.
        key = (source_currency, target_currency)
        self.rates[key] = rate

    def convert(self, amount, source_currency, target_currency):
        # Convert an amount from the source currency to the target currency.
        if (source_currency, target_currency) in self.rates:
            rate = self.rates[(source_currency, target_currency)]
            converted_amount = amount * rate
            return converted_amount
        else:
            return None  # Conversion rate not found


# Create a CurrencyConverter instance and add conversion rates.
converter = CurrencyConverter()
converter.add_rate("USD", "EUR", 0.85)
converter.add_rate("EUR", "JPY", 130.0)
converter.add_rate("USD", "JPY", 110.0)

# Convert an amount from USD to EUR and print the result.
usd_amount = 100.0
eur_amount = converter.convert(usd_amount, "USD", "EUR")
print(f"{usd_amount} USD is equivalent to {eur_amount} EUR")

# Convert an amount from EUR to JPY and print the result.
eur_amount = 50.0
jpy_amount = converter.convert(eur_amount, "EUR", "JPY")
print(f"{eur_amount} EUR is equivalent to {jpy_amount} JPY")


import numpy as np
