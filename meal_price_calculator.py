child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

drink_price = float(input("What is the price of a drink? "))
num_drinks = int(input("How many drinks were ordered? "))

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults) + (drink_price * num_drinks)
print(f"\nSubtotal: ${subtotal:.2f}")

sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

sales_tax = subtotal * (sales_tax_rate / 100)
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total (before tip): ${total:.2f}")

tip_percent = float(input("\nEnter tip percentage (e.g. 10 for 10%): "))
tip_amount = total * (tip_percent / 100)
grand_total = total + tip_amount
print(f"Tip: ${tip_amount:.2f}")
print(f"Grand Total: ${grand_total:.2f}")

payment = float(input("\nWhat is the payment amount? "))
change = payment - grand_total
print(f"Change: ${change:.2f}")
