def longest(collection):
    longest_word = max(word_list, key=len)
    return longest_word


collection = ['cat', 'horse', 'elephant', 'dog']

print("Given text: ", collection)
print("Reversed text: ", longest(collection))

