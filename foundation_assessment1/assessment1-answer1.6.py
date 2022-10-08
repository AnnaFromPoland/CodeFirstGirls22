# example of appending - we add an object to the list

my_list = ['an', 'na', 'lew']
print(my_list)
another_list = [1, 2, 3]
print(another_list)
my_list.append(another_list)
print(my_list)

# example of extending - we concatenate a list with another list (iterable)
my_list = ['foo', 'bar']
print(my_list)
another_list = [1, 2, 3]
print(another_list)
my_list.extend(another_list)
my_list = ['foo', 'bar', 1, 2, 3]
print(my_list)
