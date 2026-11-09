# csv_practice.py
# Author: Aleena Khan
# Module 12 Lab: Read a Sales CSV, write a cleaned report

import csv
from datetime import datetime 

SALES_FILE = "ddata/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("---Exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")


print("---Exercise 2---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Reflection 1:
# Reflection 2: