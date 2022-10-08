def longest(collection):
    longest_word = max(collection, key=len)
    return longest_word


collection = ['cat', 'horse', 'elephant', 'dog']

print("Given text: ", collection)
print("Reversed text: ", longest(collection))

