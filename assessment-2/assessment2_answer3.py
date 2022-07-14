import unittest


def string_length(value):
    return int(len(value))


# checks if input value is not empty


class TestIfHasLength(unittest.TestCase):
    def string_length(self):
        self.assertTrue(stringLength(value) > 0)


def divisible_by_two(value):
    return int(len(value) % 2)

# checks if it is possibly a palindrome (string is symmetrical)


class TestIfIsPossiblyAPalindrome(unittest.TestCase):
    def divisible_by_two(self):
        self.assertTrue(divisible_by_two(value) == 0)


user_input = ""

print("Hello User! Welcome to a short 'Is It a Palindrome?' program.\n"
      "It checks the word or phrase you input is a palindrome or not.\n"
      "To exit the program, hit 'X'.")

input("Please hit 'ENTER' key to continue.")


def is_palindrome(value):
    try:
        for a in range(0, int(len(value) / 2)):
            if value[a] != value[len(value) - a - 1]:
                return False
    except ValueError:
        print("You can only add numbers to your collection, please try again.")
    else:
        return True


user_input = input("Please input a word or a phrase: ")

print("Is it true the word / phrase you input is a palindrome? ", is_palindrome(user_input))
