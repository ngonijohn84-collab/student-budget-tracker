"""
W05 Project: Grocery Store Receipt

Enhancement:
- Prints a reminder of how many days remain until the New Year's Sale (Jan 1).
"""

import csv
from datetime import datetime, date


SALES_TAX_RATE = 0.06


def read_dictionary(filename, key_column_index):
    """Read a CSV file into a dictionary.

    Parameters:
        filename: name of the CSV file to read
   key_column_index: index of the column to use as the dictionary key

    Returns:
        A dictionary where each key maps to a list containing the row data
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


def main():
    try:
        # Read products dictionary
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        total_items = 0
        subtotal = 0

        # Read customer request file
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # skip header

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                # Look up product (may raise KeyError)
                product = products_dict[product_id]
                name = product[1]
                price = float(product[2])

                print(f"{name}: {quantity} @ {price:.2f}")

                total_items += quantity
                subtotal += quantity * price

        # Totals
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        print("Thank you for shopping at the Inkom Emporium.")

        # Current date and time
        current_date_and_time = datetime.now()
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

        # --- Exceeding Requirements ---
        today = date.today()
        next_new_year = date(today.year + 1, 1, 1)
        days_until_sale = (next_new_year - today).days
        print(f"New Year's Sale begins in {days_until_sale} days!")

    except FileNotFoundError as err:
        print("Error: missing file")
        print(err)

    except PermissionError as err:
        print("Error: permission denied")
        print(err)

    except KeyError as err:
        print("Error: unknown product ID in the request.csv file")
        print(err)


if __name__ == "__main__":
    main()
