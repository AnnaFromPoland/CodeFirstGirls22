# Two Number Sum -22 points
# ● write a function accepts an array of numbers and an integer representing a target sum.
# ● if any two numbers from the array == the target sum, then your function returns these numbers in an array.
# ● if no two numbers == the target sum the function should return an empty array.
# ● Note that you cannot add 1 single integer to itself in order to obtain the target sum.
# Example Input into your function:
# my_numbers = [3, 5, -4 ,8, 11, 1, -1, 6] | target_sum = 10
# Example output returned
# [-1, 11] | Numbers can be returned in any order → it does not matter

import itertools

# creating necessary variables for input
my_numbers = []
result_numbers = []
target_sum = 0
user_input = 0

# creating user input logic for number list & target sum number

print("Hello User! Welcome to a short calculation program.\n"
      "It checks if any two of the numbers from your collection add up to the 'target' number when summed.\n"
      "First please provide the collection of numbers - input 'ENTER' to exit your collection and continue.\n"
      "Then you will be asked to specify one 'target' number.")

input("Please hit 'ENTER' key to continue.")

while user_input != 'X':
    user_input = input("Please add a number to your collection or hit 'X' to exit the numbers' list: ")
    if str(user_input.upper()) != 'X':
        try:
            my_numbers.append(int(user_input))
        except ValueError:
            print("You can only add numbers to your collection, please try again.")
            continue
    else:
        print("You have input an 'X', closing your numbers collection.")
        break

print("The collection of numbers you've provided is: ", my_numbers)

while True:
    user_input = input("Please indicate the 'target' number: ")
    try:
        target_sum = int(user_input)
        break
    except ValueError:
        print("The 'target' number can only be a number, please try again.")
        continue

print("The 'target' number you've provided is: ", target_sum)

# TWO METHODS BELOW:

# # if in the condition "if any two numbers from the array == the target sum, then return these numbers in an array"
# # "return these numbers" means "return two numbers meeting the condition" as in
# # "return only 1 pair of numbers meeting the == target sum condition", this function does it:
#
# for i, j in itertools.combinations(my_numbers, 2):
#     if i + j == target_sum:
#         result_numbers.append(i)
#         result_numbers.append(j)
#         break
#
# print("These two numbers from your collection sum up to the 'target' number: ", result_numbers)

# SECOND METHOD:

# # if in the condition "if any two numbers from the array == the target sum, then return these numbers in an array"
# # "return these numbers" means "return all the number pairs meeting the condition" as in
# # "return all the pairs of numbers meeting the == target sum condition", this function does it:
#
#
# def compare(my_numbers, target_sum):
#     for i in range(len(my_numbers)):
#         for j in range(len(my_numbers)):
#             if i != j:
#                 if my_numbers[i] + my_numbers[j] == target_sum:
#                     if my_numbers[i] not in result_numbers:
#                         result_numbers.append(my_numbers[i])
#                     if my_numbers[j] not in result_numbers:
#                         result_numbers.append(my_numbers[j])
#                     break
#     return result_numbers
#
#
# print("These number pairs from your collection sum up to the 'target' number: ", compare(my_numbers, target_sum))
