import unittest


def substraction(x, y):
    return x - y


def addition(x, y):
    return x + y


class TestIfNotNegative(unittest.TestCase):
    def substraction(self):
        self.assertFalse(substraction(account_balance, withdrawal_amount) < 0)


class TestIfPositive(unittest.TestCase):
    def addition(self):
        self.assertTrue(addition(account_balance, withdrawal_amount) > 0)


class TestIfNotNull(unittest.TestCase):
    def notEmpty(self, obj):
        self.assertTrue(pin_code)


class TestIfLoggedIn(unittest.TestCase):
    def AssertTrue(self, obj):
        self.assertTrue(logged_in)


class TestIfNotMaxLoginAttempt(unittest.TestCase):
    def AssertFalse(self, obj):
        self.assertFalse(login_attempt_counter < 3)


class TooMuchError(Exception):
    pass


print("Good day! Welcome to your bank's Automated Teller Machine.")

pin_code_correct = False
login_attempt_counter = 0

while not pin_code_correct and login_attempt_counter < 3:
    try:
        pin_code = int(input("Please provide your PIN code to access your account: "))
        assert len(str(pin_code)) == 4
    except AssertionError:
        print("The PIN code must be 4 digits long.")
        login_attempt_counter += 1
    except ValueError:
        print("The PIN code must be a number.")
        login_attempt_counter += 1
    else:
        pin_code_correct = True
        print("PIN code correct, granting login access to your bank account.")

if not pin_code_correct:
    print("You've reached your 3rd attempt and the PIN code input is still incorrect, the program will terminate now.")
else:
    print("You are now logged into your bank account. Your current account balance is now 100.")

account_balance = 100
temp_account_balance = 0
deposit_amount = 0
withdrawal_amount = 0
user_action = 0
logged_in = True

while logged_in:
    user_action = int(input("Please indicate which action would you like to perform?\n"
                            "1 - Input '1' for Withdrawing Funds\n"
                            "2 - Input '2' for Depositing Funds\n"
                            "3 - Input '3' for Balance Inquiry\n"
                            "4 - Input '4' to Log Out\n"))
    match user_action:
        case 1:
            print("You chose to Withdraw Funds.")
            try:
                withdrawal_amount = int(input("Please indicate how much would you like to withdraw? "))
                if withdrawal_amount > account_balance:
                    raise TooMuchError
                else:
                    temp_account_balance = account_balance - withdrawal_amount
                    account_balance = temp_account_balance
                    print("Withdrawal successful. Your current account balance is {}.".format(account_balance))
            except TooMuchError:
                print("Your requested Withdrawal Amount is greater than your current account balance."
                      "You will now be logged out now.")
                logged_in = False

        case 2:
            print("You chose to Deposit Funds.")
            deposit_amount = int(input("Please indicate how much would you like to deposit? "))
            if deposit_amount == 0:
                print("The Deposit Amount cannot be 0, that doesn't make any sense.")
            elif deposit_amount < 0:
                print("The Deposit Amount cannot be less than 0, that doesn't make any sense.")
            else:
                temp_account_balance = account_balance + deposit_amount
                account_balance = temp_account_balance
                print("Deposit successful. Your current account balance is {}.".format(account_balance))
        case 3:
            print("You chose Balance Inquiry.")
            print("Your current account balance is {}.".format(account_balance))
        case 4:
            print("You chose to Log Out.")
            print("Goodbye!")
            logged_in = False
