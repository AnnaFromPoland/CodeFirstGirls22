# SIMPLE CALCULATOR
print("Please select operation -\n "
"1. Add\n "
"2. Subtract\n"
"3. Multiply\n"
"4. Divide\n")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

### YOUR CODE GOES HERE ###

# Function to add two numbers
sum_result = number_1 + number_2

# Function to subtract two numbers
minus_result = number_1 - number_2

# Function to multiply two numbers
multiplication_result = number_1 * number_2

# Function to divide two numbers
division_result = number_1 / number_2

# Calculator logic

switcher = {
    1: print(sum_result),
    2: print(minus_result),
    3: print(multiplication_result),
    4: print(division_result)
    }

def switch(switcher):
    return switcher.get(select)()


