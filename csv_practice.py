# csv_practice.py
# Author: Aleena Khan
# Module 12 Lab: Read a Sales CSV, write a cleaned report

import csv
from datetime import datetime 

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"


# Exercise 1:
print("---Exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")


# Exercise 2:
print("---Exercise 2---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



# Exercise 3:
print("---Exercise 3---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader) # next() returns the next item from the iterator, which is the header row
    print(f"Header: {header}")
    for row in reader:
        print(row)


# Exercise 4:
print("---Exercise 4---")
total_revenue = 0 
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row # unpacking
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")


# Exercise 5:
print("---Exercise 5---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")


# Exercise 6:
print("---Exercise 6---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${dict_total:.2f}")
# Use standard csv.reader for positional data without headers
# Use csv.DictReader when headers exist to reference columns by name


# Exercise 7:
print("---Exercise 7---")
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


# Exercise 8:
print("---Exercise 8---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE,"r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")


# Reflection 1: Python automates large data pipelines faster than Excel. Excel handles quick visual edits easier than code.
# Reflection 2: An online store tracking customer transactions uses an order log. Append mode adds new records safely without overwriting past data.