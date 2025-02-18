class Savings_Account:
    
    # Constructor with default attribute values
    def __init__(self):
        self.currency_name = "default currency name"
        self.principal_amount = 0.0
        self.interest_rate = 0.0
        self.number_of_years = 0.0

    # Getters for class attributes
    def get_currency_name(self):
        return self.currency_name
    
    def get_principal_amount(self):
        return self.principal_amount
    
    def get_interest_rate(self):
        return self.interest_rate
    
    def get_number_of_years(self):
        return self.number_of_years
    
    # Setters for class attributes
    def set_currency_name(self, new_currency_name):
        self.currency_name = new_currency_name

    def set_principal_amount(self, new_principal_amount):
        self.principal_amount = new_principal_amount

    def set_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate
    
    def set_number_of_years(self, new_number_of_years):
        self.number_of_years = new_number_of_years

    # Calculates balance of savings account after interest accrues
    # Uses yearly compounding interest formula: A = P(1 + r)^t
    # A = Resulting amount
    # P = Principal amount
    # r = Interest rate -- This must be divided by 100 to convert to decimal form
    # t = Number of years interest accrues
    # Resulting amount is rounded to the nearest hundredth
    def calculate_balance_after_interest(self):
        balance_after_interest = self.principal_amount * (1 + (self.interest_rate / 100)) ** self.number_of_years
        balance_after_interest = round(balance_after_interest, 2)
        return balance_after_interest
    
    # Prints savings account balance after interest accrues
    def print_balance_after_interest(self):
        try:
            print("After yearly compounding interest, your account would have " + str(self.calculate_balance_after_interest()) + " " + self.get_currency_name())
        except OverflowError:
            print("Your account would have more money than this calculator can handle!  Try something smaller.")