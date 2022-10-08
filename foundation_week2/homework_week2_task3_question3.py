# omelette maker

# 1 decide the size of your omelette - how many eggs do you want to make 1 omelette of?
# 1 change the value of omelette_size if you want your omelettes made smaller or bigger (from more or less eggs)
omelette_size = 4  # value given in the example was 4, you want your omelettes made of 4 eggs each

# 2 disclose the size of your egg box - this program assumes that you buy same size of egg boxes, not mixed sizes
# 2 change the value of eggs_in_one_box if you buy boxes containing different number of eggs
eggs_in_one_box = 6  # value given in the example was 6, you prefer small egg boxed with only 6 eggs inside each

# 3 disclose how many boxes of eggs you have - this program assumes all boxes are full, not partially full
# 3 change the value of how_many_boxes_of_eggs when the number of full boxes of eggs you have changes
how_many_boxes_of_eggs = 5  # value given in the example was 5, you have 5 boxes of eggs

# 4 formula that calculates the answer to "how many omelettes can i make from the number of boxes of 6 eggs each
how_many_omelettes = (eggs_in_one_box * how_many_boxes_of_eggs)/omelette_size

# 5 formatting the message conveying the answer in full sentence
# 5 i cast how_many_omelettes to integer because it's in reality unfeasible to make 0.5 an omelette - irl you
# only make full omelettes, irl you only make full omelettes, so the remainder of eggs (3 in our example case)
# would simply stay in the fridge, not be used to make a 0.5 an omelette.
message = 'You can make {} omelettes with {} boxes of eggs'.format(int(how_many_omelettes), how_many_boxes_of_eggs)

# 6 providing the message with the answer to the user
print(message)