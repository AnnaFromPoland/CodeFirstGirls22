book_publishing_year = int(input("What year was this book published in? (input a numerical year value) : "))
book_publishing_century_input = int(str(book_publishing_year)[1:2])
book_publishing_decade_input = int(str(book_publishing_year)[2:3])
book_publishing_century_output = " "
book_publishing_decade_output = " "

if book_publishing_century_input == 8:
    book_publishing_century_output = "19th century"
elif book_publishing_century_input == 9:
    book_publishing_century_output = "20th century"
else:
    book_publishing_century_output = "a different century"

match book_publishing_decade_input:
    case 0:
        book_publishing_decade_output = "Aughts"
    case 1:
        book_publishing_decade_output = "Teens"
    case 2:
        book_publishing_decade_output = "Twenties"
    case 3:
        book_publishing_decade_output = "Thirties"
    case 4:
        book_publishing_decade_output = "Forties"
    case 5:
        book_publishing_decade_output = "Fifties"
    case 6:
        book_publishing_decade_output = "Sixties"
    case 7:
        book_publishing_decade_output = "Seventies"
    case 8:
        book_publishing_decade_output = "Eighties"
    case 9:
        book_publishing_decade_output = "Nineties"

print("This book was published in {}, in the {}.".format(book_publishing_century_output, book_publishing_decade_output))
