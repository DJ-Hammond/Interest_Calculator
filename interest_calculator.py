# Import Savings_Account class
from savings_account import Savings_Account

# Checks all characters in a string and returns true if any are numbers
def contains_numbers(string_checked_for_numbers):
    return any(character.isdigit() for character in string_checked_for_numbers)

# Constructs a Savings_Account object that represents the user's interest-accruing account
user_savings_account = Savings_Account()

# Infinite loop to let user continue performing calculations
# Breaks if user doesn't enter continue command after calculations
while True:

    # Infinite loop to get a valid currency name from the user
    # A valid currency name must contain only letters and spaces, and must not have numbers
    while True:
        user_currency_name = input("What type of currency are you using? ")
        if user_currency_name.replace(" ", "").isalpha() and user_currency_name != "":
            user_savings_account.set_currency_name(user_currency_name)
            break
        elif contains_numbers(user_currency_name):
            print("Please enter a currency name without numbers.")
        elif user_currency_name == "":
            print("Please enter a non-empty currency name.")
        else:
            print("Please enter a valid currency name.")
    
    # Infinite loop to get a valid principal amount from the user
    # A valid principal amount must be a non-negative number
    while True:
        try:
            user_principal_amount = float(input("What is your starting principal amount? (Do not include any symbols other than a decimal point) "))
            if user_principal_amount >= 0:
                user_savings_account.set_principal_amount(user_principal_amount)
                break
            else:
                print("Please enter a non-negative number.")
        # Handles non-numeric input
        except ValueError:
            print("Please enter a valid number.")

    # Infinite loop to get a valid interest rate from the user
    # A valid interest rate must be a non-negative number
    while True:
        try:
            user_interest_rate = float(input("What is the interest rate percentage? (Do not include the percentage sign) "))
            if user_interest_rate >= 0:
                user_savings_account.set_interest_rate(user_interest_rate)
                break
            else:
                print("Please enter a non-negative number.")
        # Handles non-numeric input    
        except ValueError:
            print("Please enter a valid number.")

    # Infinite loop to get a valid number of years from the user
    # A valid number of years must be a non-negative number
    while True:
        try:
            user_number_of_years = float(input("How many years will interest accrue? (Do not include the word \"years\") "))
            if user_number_of_years >= 0:
                user_savings_account.set_number_of_years(user_number_of_years) 
                break
            else:
                print("Please enter a non-negative number.")
        # Handles non-numeric input
        except ValueError:
            print("Please enter a valid number.")
    
    # Print savings account balance after interest accrues
    user_savings_account.print_balance_after_interest()

    # Ask user to continue or quit
    # Continue command is not case sensitive
    response = input("If you would like to continue, type y.  Anything else will quit. ")
    if response.casefold() != "y":
        break
