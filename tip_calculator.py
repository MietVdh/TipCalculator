# Import math library to use math.ceil (to get next integer up)
import math

# Calculate the amount of tax from the before-tax amount and tax rate
def calculateTax(pre_tax_amount, tax_rate):
    return round(pre_tax_amount + (pre_tax_amount * tax_rate), 2)

# Calculate the before-tax amount if after-tax amount is given
def calculatePreTaxAmount(after_tax_amount, tax_rate):
    return round(after_tax_amount/(1 + tax_rate), 2)


# Calculate tip and total amount
def calculate_tip(pre_tax_amount, tax_amount, tip_percentage):
    tip = round(pre_tax_amount * tip_percentage, 2)
    total = pre_tax_amount + tax_amount + tip
    return (tip, total)

# Increase tip to round up total to next dollar amount
def round_up_tip(total, tip):
    # Check if total is already an integer; if not, round
    if (not isinstance(total, int)):
        rounded_total = math.ceil(total)
        difference = round(rounded_total - total, 2)
        tip += difference
        total = rounded_total
    return tip, total


# Check with user if they want to enter the before or after tax amount
def get_option():
    option = ""
    # Keep asking for an option until user enters either "A" or "B"
    while not (option == "A" or option == "B"):
        option = input("Do you have the before or after tax amount? Enter 'B' for before; 'A' for after\n").upper()
    return option


# Get pre-tax amount and tax rate from user
# Calculate tax
# Return pre-tax amount and tax
def get_pre_tax_amount():
    pre_tax_amount = 0
    tax_rate = 0
    # Keep asking for input until input given is valid
    while not pre_tax_amount:
        try:
            pre_tax_amount = float(input("Please enter the total pre-tax amount:\n"))
        except(Exception):
            continue
    while not tax_rate:
        try:
            tax_rate = float(input("Please enter the tax rate as a percentage (no percentage sign). e.g. '12.5':\n"))
        except(Exception):
            continue
    # Calculate tax amount
    tax = round(calculateTax(pre_tax_amount, (tax_rate/100)), 2)
    return (pre_tax_amount, tax)

# Get after-tax amount and tax rate from user
# Calculate pre-tax amount and tax
# Return pre-tax amount and tax
def get_pre_from_after_tax_amount():
    after_tax_amount = 0
    tax_rate = 0
    # Keep asking for input until input given is valid
    while not (after_tax_amount and after_tax_amount > 0):
        try:
            after_tax_amount = float(input("Please enter the total after-tax amount:\n"))
        except(Exception):
            continue
    while not (tax_rate and tax_rate < 100 and tax_rate >= 0):
        try:
            tax_rate = float(input("Please enter the tax rate as a percentage (no percentage sign). e.g. '12.5':\n"))
        except(Exception):
            continue
    # Calculate the pre-tax amount
    pre_tax_amount = calculatePreTaxAmount(after_tax_amount, (tax_rate/100))
    # Calculate the tax amount
    tax = round(after_tax_amount - pre_tax_amount, 2)
    return (pre_tax_amount, tax)

# Get tip percentage the user wishes to tip
# Return tip percentage (as a floating point number; e.g. "0.18")
def get_tip_percentage():
    tip_percentage = 0
    # Keep asking for input until input is valid (i.e. a positive number)
    while not (tip_percentage and tip_percentage > 0):
        try:
            tip_percentage = float(input("Please enter the tip percentage you would like to add (no '%' signs, please). E.g. '18':\n"))
        except Exception:
            continue
    return tip_percentage/100


# Display the subtotal, tax, tip, and total amounts
def output_info(pre_tax, tax, tip, total):
    print("\nThis is what your bill looks like:\n")
    print("Subtotal (before tax): \t" + (pre_tax))
    print("Tax:\t\t\t" + str(tax))
    print("Tip:\t\t\t" + str(tip))
    print("Total:\t\t\t" + str(total))


# Calculate tax, tip, total after getting the required info from the user
def get_info(option):
    pre_tax_amount = 0
    tax = 0

    if option == "B":
        # Use before tax amount
        pre_tax_amount, tax = get_pre_tax_amount()

    elif option == "A":
        # Use after tax amount
        pre_tax_amount, tax = get_pre_from_after_tax_amount()

    tip_percentage = get_tip_percentage()

    tip, total = calculate_tip(pre_tax_amount, tax, tip_percentage)
    return  pre_tax_amount, tax, tip, total


# Main program

# initialize variables
pre_tax_amount = 0
tax = 0
tip = 0

# Print introduction and instructions
print("Welcome to the Tip Calculator!")
print("We will need the total amount for your bill, either before or after tax, as well as the tax rate")

# Ask for option (before- or after-tax amount)
option = get_option()
# Get numbers (subtotal, tax rate, tip)
pre_tax_amount, tax, tip, total = get_info(option)
# Display the amounts
output_info(pre_tax_amount, tax, tip, total)

# Give user option to round up total amount to nearest dollar if not already an integer
if not isinstance(total, int):
    if (input("Would you like to round the total up to the nearest dollar? Enter Y for yes; any key for no\n")).upper() == "Y":
        tip, total = round_up_tip(total, tip)
    output_info(pre_tax_amount, tax, tip, total)
