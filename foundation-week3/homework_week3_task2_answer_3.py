import random

print("Please choose 7 numbers for your lottery ticket. Hit ENTER key when ready.")

# declaring and initialising side variables used in lottery ticket generating logic

which_number = 0
which_number_ordinal = ''


def match_function(which_number):
    match which_number:
        case 0:
            return '1st'
        case 1:
            return '2nd'
        case 2:
            return '3rd'
        case 3:
            return '4th'
        case 4:
            return '5th'
        case 5:
            return '6th'
        case 6:
            return '7th'


# # LOTTERY TICKET GENERATING LOGIC - METHOD 1 - random sample of 7 numbers >100 auto generated with random function
#
# lottery_ticket = random.sample(range(100), 7)

# LOTTERY TICKET GENERATING LOGIC - METHOD 2 - list of 7 zeros, user updates value of each list item by input

lottery_ticket = [0, 0, 0, 0, 0, 0, 0]
for i in range(len(lottery_ticket)):
    which_number_ordinal = match_function(which_number)
    lottery_ticket[i] = int(input("Please choose your {} lottery ticket number: ".format(which_number_ordinal)))
    which_number += 1

# # LOTTERY TICKET GENERATING LOGIC - METHOD 3 - list size 0 (empty), each user input number appends to the list
#
# lottery_ticket = []
# i = 0
# while i < 7:
#     which_number_ordinal = match_function(which_number)
#     lottery_ticket.append(int(input("Please choose your {} lottery ticket number: ".format(which_number_ordinal))))
#     which_number += 1
#     i += 1

print("Your lottery ticket numbers are: ", lottery_ticket)

# lottery result generating logic (random sample, non repeatable)

lottery_result = random.sample(range(100), 7)
print("The results of today's draw are: ", lottery_result)

# lottery match number deciding logic

number_of_matches = 0

for i in lottery_ticket:
    for j in lottery_result:
        if j == i:
            number_of_matches += 1
        else:
            continue

your_prize = 0

# lottery prize deciding logic

match number_of_matches:
    case 3:
        your_prize = 20
    case 4:
        your_prize = 40
    case 5:
        your_prize = 100
    case 6:
        your_prize = 10000
    case 7:
        your_prize = 1000000

# lottery result & prize announcement

print("You had {} matching numbers and have won the {}GBP prize! Congratulations!"
      .format(number_of_matches, your_prize)) if your_prize > 0 else print(
    "You had no matching numbers and have not won anything at this lottery. Better luck next time!")

# the code works but the rng is cruel, increase lottery result range to 30 results for more matches -> faster validation
