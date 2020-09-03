print("Loading.......")

import currency_exchange

currency_from = input("From currency (Use abreviation)")
currency_to = input("To currency (Use abreviation)")
amount = input("Amount (only whole numbers): ")

try:
    amount2 = int(amount)
except ValueError:
    amount2 = float(amount)

FINAL = currency_exchange.exchange(currency_from, currency_to, amount, True)

print(FINAL)
