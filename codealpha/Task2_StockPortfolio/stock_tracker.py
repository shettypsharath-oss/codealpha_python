stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter stock name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    value = stocks[stock] * quantity
    total += value

    print("Investment:", value)

print("\n==============================")
print("Total Investment: ₹", total)
print("==============================")

with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Report\n")
    file.write("======================\n")
    file.write("Total Investment: ₹" + str(total))

print("Report saved as portfolio.txt")