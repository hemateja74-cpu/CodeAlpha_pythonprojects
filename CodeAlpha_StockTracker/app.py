import csv
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 2800,
    "AMZN": 3450
}

def main():
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    portfolio = {}

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == "DONE":
            break
        if symbol not in stock_prices:
            print("❌ Stock not found. Try again.")
            continue

        try:
            qty = int(input(f"Enter quantity of {symbol}: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + qty

    print("\n📊 Portfolio Summary:")
    total_value = 0
    for symbol, qty in portfolio.items():
        value = qty * stock_prices[symbol]
        total_value += value
        print(f"{symbol} - {qty} shares → ${value}")

    print(f"\n💰 Total Investment Value: ${total_value}")

    save = input("Do you want to save this portfolio to portfolio.csv? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for symbol, qty in portfolio.items():
                writer.writerow([symbol, qty, stock_prices[symbol], qty * stock_prices[symbol]])
            writer.writerow(["Total", "", "", total_value])
        print("✅ Portfolio saved to portfolio.csv")

if __name__ == "__main__":
    main()



