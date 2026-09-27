stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "META": 500
}

print("=" * 50)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

portfolio = {}
total_investment = 0

try:
    num_stocks = int(input("\nHow many different stocks do you want to add? "))

    if num_stocks <= 0:
        print("Please enter a number greater than 0.")
        exit()

    for i in range(num_stocks):
        stock = input(f"\nEnter stock symbol #{i + 1}: ").upper()

        if stock not in stock_prices:
            print("Stock not found in the available stock list.")
            print("Please choose from:", ", ".join(stock_prices.keys()))
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            portfolio[stock] = portfolio.get(stock, 0) + quantity

        except ValueError:
            print("Please enter a valid quantity.")

    print("\n" + "=" * 50)
    print("          YOUR STOCK PORTFOLIO")
    print("=" * 50)

    if not portfolio:
        print("No stocks were added to the portfolio.")
        exit()

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Value':<12}")
    print("-" * 50)

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value

        print(f"{stock:<10}{quantity:<12}${price:<11}${value:<11}")

    print("-" * 50)
    print(f"Total Investment: ${total_investment:,.2f}")
    print("=" * 50)

    save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio_result.txt", "w") as file:
            file.write("STOCK PORTFOLIO TRACKER\n")
            file.write("=" * 40 + "\n\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity

                file.write(
                    f"{stock} | Quantity: {quantity} | "
                    f"Price: ${price} | Value: ${value}\n"
                )

            file.write("\n" + "=" * 40 + "\n")
            file.write(f"Total Investment: ${total_investment:,.2f}\n")

        print("\nResult saved successfully to 'portfolio_result.txt'.")

    print("\nThank you for using Stock Portfolio Tracker!")

except ValueError:
    print("\nInvalid input! Please enter a valid number.")
