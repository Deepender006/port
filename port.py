# Predefined stock prices (manual entry)
stock_prices = {
    "AAPL": 195.56,
    "GOOGL": 2824.72,
    "MSFT": 352.12,
    "TSLA": 267.85,
    "AMZN": 133.53
}

# Dictionary to store shares owned
stock_shares = {}

# Input shares owned for each stock
print("📊 Simple Stock Tracker")
print("Enter how many shares you own for each stock:\n")

for stock in stock_prices:
    while True:
        try:
            shares = int(input(f"{stock}: "))
            if shares < 0:
                raise ValueError
            stock_shares[stock] = shares
            break
        except ValueError:
            print("❌ Please enter a valid positive number.")

# Calculate and display total investment
total_value = 0
print("\n💼 Investment Summary:")
for stock in stock_prices:
    shares = stock_shares[stock]
    price = stock_prices[stock]
    value = shares * price
    total_value += value
    print(f"{stock}: {shares} shares × ${price:.2f} = ${value:.2f}")

print(f"\n🔢 Total Investment Value: ${total_value:.2f}")
