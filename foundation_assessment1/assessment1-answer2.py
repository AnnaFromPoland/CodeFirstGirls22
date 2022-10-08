with open('my_file.txt') as fh:
text = fh.read()
big_letters_count = 0
for i in text:
      if i.isupper():
            big_letters_count += 1
print("Upper Letters in Given Text: ", big_letters_count)
