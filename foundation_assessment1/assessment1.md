# Assessment 1
#### 1.1 What is Python? What are the benefits of using python?
Python is a programming language. It’s OOP and interpreted (doesn’t need to compile). It’s not typed like Java. Pluses: similar to spoken language, intuitive for that. Not typed can be a plus. Not compiled is a plus -> faster. Not typed can also be a minus due to possible errors.
#### 1.2 What does ‘string’ method count() do, provide an example.
It counts how many times the text given in brackets appears in a strong.
EXAMPLE:

    txt = "I like music, chocolate, cinnamon and games."
    x = txt.count("music")
    print(x)

#### 1.3 What do functions ord() and chr() do, provide examples
chr() is used for converting an Integer to a Character
ord() is used to convert a Character to an Integer
EXAMPLE:

    print(chr(0x41))
    i = ord('A')
    print(i)

#### 1.4 Given string ‘2020-11-10_sales.csv’ how can I get ‘2020-11-10_sales’ using slicing ?

    txt = '2020-11-10_sales.csv'
    print(txt[:-4])

#### 1.5 What is the difference between List and Tuple data types in Python?
Lists have [], tuples have (), tuples are faster, tuples are immutable, lists are changeable, lists are better for performing the DML operations (insert, delete etc.) and have some methods while tuples do not.

#### 1.6 What is the difference between List methods append() and extend(), provide examples.
Append adds new element(s) to an existing lists, can be an object. It adds an item at the end of the list appending it. Extend also adds, but it adds elements from another iterable list.

Example of appending - we add an object to the list:

    my_list = ['an', 'na', 'lew']
    print(my_list)
    another_list = [1, 2, 3]
    print(another_list)
    my_list.append(another_list)
    print(my_list)

Example of extending - we concatenate a list with another list (iterable):

    my_list = ['foo', 'bar']
    print(my_list)
    another_list = [1, 2, 3]
    print(another_list)
    my_list.extend(another_list)
    my_list = ['foo', 'bar', 1, 2, 3]
    print(my_list) 

#### 1.7 What does ‘infinite loop’ mean and how to avoid it?
Infinite loop means a loop will go on forever, because it either does not have an exit condition or the exit condition is never met. We can avoid having our loop run indefinitely by 1 – providing an exit condition (such as “if i = 0” or “if you run to the end of the table then stop iterating”) and 2 – making sure that for our data the possibility of this condition becoming true exists.

#### 1.8 What does function ‘parameters’ and function ‘arguments’ mean?
Function parameters are the variables (names of the variables) which the function can use. When declaring a function one should declare the parameters it (the function) can operate on. Parameters are the values these variables are given. These values are then worked by the function to provide an output (some result).

#### 1.9 How to add a new key, value pair to a dictionary, provide examples.
Using either the subscript or the update() method.

    dict = {'a1': 'nut choco', 'a2': 'snickers', 'a3': 'choco plum'}
    print("Currently Possessed Sweets: ", dict)

Example - adding new key and value by substring:

    dict['a4'] = 'mars bar'
    dict['a5'] = 'gummy bear'
    print("Updated Sweets Repo: ", dict)

Example - adding new key and value using method update():

    dict.update({'a6': 'cream fudge'})
    print("Even Bigger Sweets Repo: ", dict)

#### 1.10 Place these data types into one of the two categories
MUTABLE: list, set, dict
IMMUTABLE: bool, int, tuple, str

#### 2 If you would need to count all of the capital letters in a file. How would you do it?

    with open('my_file.txt') as file:
    text = file.read()
    big_letters_count = 0
    for i in text:
          if i.isupper():
                big_letters_count += 1
    print("Upper Letters in Given Text: ", big_letters_count)
    
Kindly please also find the code answer to this question saved as "assesment1-answer2.py" file.

#### 3 Given any string, reverse it, so that it reads backwards, for example: if the string is “Apple”, you get “'elppA”. You can do this in any way you want.

    def reverse(text):
        rev = ''
        for i in text:
            rev = i + rev
        return rev
    
    
    text = 'Apple'
    
    print("Given text: ", text)
    print("Reversed text: ", reverse(text))

Kindly please also find the code answer to this question saved as "assesment1-answer3.py" file.

#### 4 Write a function to find the longest word in the list of strings. Given [‘cat’, ‘horse’, ‘elephant’, ‘dog’] your function would return ‘elephant’.

    def longest(collection):
        longest_word = max(collection, key=len)
        return longest_word
    
    
    collection = ['cat', 'horse', 'elephant', 'dog']
    
    print("Given text: ", collection)
    print("Reversed text: ", longest(collection))

Kindly please also find the code answer to this question saved as "assesment1-answer4.py" file.

#### 5 Write a simple calculator which can perform basic arithmetic operations like addition, subtraction, multiplication or division depending upon the user input.
Answer: below is a calculator that works. It’s the simpliest one I could think of, but it gives all results regardless of choice because I don’t know how to include “break” in Python, I know how to do this in Java. I don’t have time, I have like 15mins left now for SQL because I spend so much time editing this file ;_;

SIMPLE CALCULATOR

    print("Please select operation -\n "
    "1. Add\n "
    "2. Subtract\n"
    "3. Multiply\n"
    "4. Divide\n")
    
    # Take input from the user
    select = int(input("Select operations form 1, 2, 3, 4 :"))
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    
    # Calculator operations
    sum_result = number_1 + number_2
    minus_result = number_1 - number_2
    multiplication_result = number_1 * number_2
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
        
        

Kindly please also find the code answer to this question saved as "assesment1-answer5.py" file.

#### 6.1 What is MySQL?
It’s a language made by Oracle to make queries to databases called “Structured Query Language”. It makes questions, calls, and operations on database data and database structure as well.

#### 6.2 Difference between CHAR and VARCHAR?
VARCHAR is longer, CHAR is up to 30 characters while varchar can take 0 to 255. There are also differences in storage and retrieval but that’s as of now a bit beyond my comprehension level.

#### 6.3 What do you mean by % and _ in the LIKE statement?
% is a wildcard – can be any sign or a number of signs, can be at the beginning, in the middle, or at the end of a value. (I have to end this test now…)
[added after the assessment, to have a fully answered file] 
The placement of this sign indicates the pattern - %a would mean any content ending with an a, a% would mean any content beginning with an a.  The difference between _ and % signs is that _ always represents exactly one character while % can represent any number of characters - zero, one, however many.
In MS Access % is * and _ is ?

#### 6.4 What is the difference between WHERE and HAVING clause?
[added after the assessment, to have a fully answered file] Hierarchy - WHERE precedes HAVING, having is used after WHERE to further filter the query results. WHERE can be the last qualifying filter ot GROUP BY and HAVING can follow, while HAVING might be the last qualifying filter but it must be preceded by GROUP BY filter. WHERE is used to qualify the result of our query using some condition in order not to provide all of the table rows (cuts out the rows not meeting this condition from the returned result), while HAVING further filters that group down using some condition provided (further cuts out from the answer provided). HAVING can be used only with SELECT query statements while WHERE can be used also with UPDATE and DELETE statements. WHERE operates on rows, so excludes or includes data based on rows, and operates only with single row functions, while HAVING operates on columns, so can also execute functions like COUNT or SUM.

#### 6.5 What does CHECK constraint do, give an example?
[added after the assessment, to have a fully answered file] The CHECK constraint is another way to limit the answers returned to us as a result of running an SQL query. It will check for the requirement and only return the results meeting the requirement. We can set a limit for example, and return values above or below that value. Constrained can be applied on a column or on the whole table.

EXAMPLE - CHECK restraint on a column:

    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        CHECK (Age>=18)
    );

EXAMPLE - CHECK constraint on a table:

    ALTER TABLE Persons
    ADD CHECK (Age>=18);

#### 6.6 Name ANY 3 types of JOINs with simple examples (you can draw circle diagrams or explain?
[added after the assessment, to have a fully answered file] There are 5 types, but one is a bit odd.
(INNER) JOIN: Returns records that have matching values in both table.
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
SELF JOIN: (the odd one) If there are two tables which are identical but differently named, they can be joined with a self join. 

The below images display the general idea behind the differences between these joins (general logic)
(insert images)

The below examplle showcases exactly how these general logic works in practice - which records get joined with which joining method, and which get omitted.
(insert image)

#### 6.7 What are COMMIT and ROLLBACK in transaction?
[added after the assessment, to have a fully answered file] COMMIT and ROLLBACK are the opposite commands when it comes to their execution. Just like in GitHub COMMIT is for committing the changes, so confirms and applies them. Unlike in GitHub there is no need to push them after this, committing is the final step that does apply the changes we've crafted to the data. Also unlike in GitHub, which is a version control device, changes applied with COMMIT cannot be rolled back afterwards. It's possible to undo them by the usual route of data overwriting, how this data got there in the first place, but the changes cannot be simply undone. ROLLBACK is the opposite of COMMIT, it rolls the changes we were crafting (not committed yet) back, so anything we're trying to do, it pulls back any and all changes. This applies to the uncommitted changes in the current session/transaction, not to any already saved changes in the previous sessions/transactions.

#### 6.8 What is the difference between these aggregate functions: COUNT() and SUM()?
[added after the assessment, to have a fully answered file] I think it's the same in Excel - counting counts occurrence, and sum sums the values - so for example, if we have a column with values like 2, 4, 2, 3, 1, 6, 8 - the function count() will count how many numbers are there in a given column (or any other given qualification we provide to apply) so would say that count is 7, and the function sum() will add the values of all the 7 items, so the result of this function will be 26.

#### 6.9 What do you mean by Stored Procedures? How do we use it?
[added after the assessment, to have a fully answered file] A stored procedure is a procedure that has been pre prepared, written and saved in the project for later use. It means we don't need to write it anew each time, we can isntead just call it to use it (execute it), because it is written already. The procedure is a set of statements, it can be a query or some command, function that does something or a mix of everything. Anyway, if that action is something that we predict to do often on our database, we can write it once, store it as a procedure, and then next time just call its name instead of writing all the statements anew. 

Example of creating a stored procedure:

    CREATE PROCEDURE procedure_name
    AS
    sql_statement
    GO;

Where the sql_statement is the place where all the statements, queries and functions we would like to proceduralise should go.

To access and run a stored procedure we just need to call its name:

    EXEC procedure_name;

#### 6.10 What is the difference between clustered and non-clustered indexes?
The key differences between these two indexes are:
- Clustered index sorts the rows of the table, non-clustered does not
- Clustered index relies on a primary key (non-repeatable, unique key)
- In 1 table, there can be only 1 clustered index (because 1 set of data (table) can be only sorted in 1 way at a time – because sorting all the rows in the table according to 1 unrepeatable key affects all the rows)
- 1 table can have 1 or more non-clustered indexes
- Non-clustered index stores the information about the location of the data (using a certain indexing key to refer to the data by) separately from the table, not inside the table
- Clustered index is called “clustered” because it uses one or more columns to index (can use more than 1 column to index)
- Clustered index stores key + data together
- Clustered is called “primary” and non-clustered a “secondary” index

Sources:
https://docs.microsoft.com/en-us/sql/relational-databases/indexes/clusteredand-nonclustered-indexes-described?view=sql-server-ver16 ;
https://www.ibm.com/docs/en/ias?topic=indexes-clustered-non-clustered
https://www.javatpoint.com/mysql-clustered-vs-non-clustered-index
https://www.guru99.com/clustered-vs-non-clustered-index.html
https://www.geeksforgeeks.org/difference-between-clustered-and-nonclustered-index