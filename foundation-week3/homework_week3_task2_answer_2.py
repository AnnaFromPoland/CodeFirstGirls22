chocolates = {
	'white': 1.50,
	'milk': 1.20,
	'dark': 1.80,
	'vegan': 2.00,
}

choice = input("Which chocolate do you desire?\nWhite,\nMilk,\nDark,\nVegan?\n"
               "Type the name of your chosen chocolate type: ").lower()
print("Here's the {} chocolate, please prepare {}GBP as payment.".format(choice, chocolates.get(choice)))
