# ASSESSMENT 
# Python Full-stack Stream, assessment test 2 hours 
# SECTION TYPE
# TOTAL MARKS AVAILABLE
# NOTES
Complexity Analysis 
25
Multiple questions, all comprising 25 total
Algorithms 1  (Coding)
25
1 question only
Algorithms 2 (Coding) 
25
1 question only
Concept Generation & Prototype (Design)
25
1 question only. Essay-based answer is needed
100 marks available total

Please note:
This is a closed book exam - 2 hours in length.
You are allowed to use PyCharm or any other tool as you see fit (but no googling! Unless it's for looking-up documentation or syntaxes: other than that, please don’t outright cheat as we will know + it’s good to be ethical!).
You are given this PDF and / or Word document alongside a Python file (e.g. ‘code environment’). This .py contains skeleton code for you to modify, for the algorithm questions, as well as sample test cases that you can use to test your solution! 
Please leave your code in the .py file, and your submission for Q1 and Q4 in either .py file (please just document / format it nicely for easier marking) or as a separate marked file (e.g. word document).
Also - when submitting, make sure to rename all the files you’re passing to include your name - this makes marking a lot easier!
Finally - best of luck! Remember, this is not a determinant of your talent. This test is simply to assess your ability, see where you can grow, as well as push you out of your comfort zone. Stay calm, deep breaths, you got this!

## Complexity Analysis
25 total (each question is worth 5)
Describe the average Big O complexity (both Time and Space) of the following code samples and / or problem samples (no code). Each answer is worth 5 marks (2.5 for Time, 2.5 for Space).

#### Code Sample 1 (5 marks):

This is a hashing-based approach for solving the Two Sum problem. Given an input array of integers and a target, it scours the array until it’s able to find two numbers that add up to the target. If no such pair can be found, then it returns an empty array.
What is the Big O Time and Space complexity of this code?

#### ANSWER:

The Big O notation for this is N squared so O(n2) where two should be uppercased but I don't know how to write that in .md file - this is because for each number in the array of numbers the algorithm needs to check up to all other numbers to find a pair - if pair is found sooner, good, but pair can be the last number checked, so it's the n number times n numbers (all other numbers in the array). n * n gives n squared. This means it's a rather costly algorithm and its time space complexity will rise drastically as the array lengthens (rises in length).

#### Problem Sample 2 (5 marks):

I have a Graph data structure that has N number of nodes (a small sample representative of it is depicted via the image above). My hypothetical code runs a Depth First Search algorithm on it - that is, I’d like to traverse all nodes in order to store their values (e.g. add node.value to my collection). For my algorithm, I use a stack data structure to hold the order of the nodes (e.g. visit node A, then node B, then node C). My algorithm is effectively just DFS.
What is the Big O Time and Space complexity of this code?

#### ANSWER:

I'm not sure storing the values can be understood as an index if we're using stacking, because with stacking we still need to go through all the elements above the one we want to reach to get to it. I think because this means all elements would be accessed once to map them in a new collection, and some items will be accessed once again to retrieve some item we want, the Big O notation is around O(n + (0.5n2)) [meaning one n plus half an n squared - with each iteration that half n squared will keep decreasing, as 0.5 squared gives 0.25 squared, so it gets halved effectively]. This makes this algorithm faster, some items are not accessed second time.

#### Code Sample 3 (5 marks):

I regularly receive text like “abcdcba” and have devised an algorithm that can tell me whether the text is a palindrome or not. For “abcdcba” it returns False, whereas for text like “a” or “aba” it returns True (single-characters count as palindrome too!). This is a pointer-based approach to the Palindrome problem; I set a pointer to the left and another to the right, and slowly move them to the middle.
What is the Big O Time and Space complexity of this code?

#### ANSWER:

I think this algorithm is O(n) because each character is only accessed once. We start from left and right, move by 1 character, and there is also the left < right logic which ensures that once we reach the middle (and this logical argument no longer resolves to true, and our loop wont run anymore) our code will stop checking - this ensures we only read each half of the string once, each character once. Therefore the complexity is only equal to as many characters our array has, so = n. This is a fast algorightm and an efficient one.

#### Problem Sample 4 (5 marks):

No image for this problem unfortunately. Given a sorted array containing integer numbers and an integer target, I conduct a search algorithm on it in order to see if the target is present in that array or not. If it is, I return the index it was found at, else I return -1 to denote that it is not inside that array. My approach mirrors, if not is identical and effectively the same as, Binary Search. That is:
    • I select the middle of the array
    • I examine the middle element - if its bigger than my target, I dispose the right-half and only examine the left half (left of the target, where all the array elements are smaller)
    • If it’s bigger, then I do the opposite
    • I repeat until there is no more to search, or my middle element matches my target
    • Effectively, Binary Search
    • Hint: Each iteration, I dispose half of the search space / array each time. The array gets halved per iteration.
What is the Big O Time and Space complexity of this code?

#### ANSWER:

I think for this one the answer is that Big O notation is O(0.5n2) so half n squared (I remember that squares of halves and one quarters and so forth just go smaller, which is very fitting in this case, as with each iteration, our search "field" gets smaller - if a half is halved, it gives a quarter, if that is halved, it gives an eigth and so forth).

## Algorithms 1 (Coding)
25 (1 question)
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.
For example, some sample input and outputs would be:

Array value
Sequence value
Output
Why?
Sample Input 1
[5, 1, 22, 25, 6, -1, 8, 10]
[1, 6, -1, 10]
true
All elements of the sequence are contained in the ‘Array’, even if they’re not contiguous in the input array
Sample Input 2
[5, 8, 3, -2, 4]
[8]
true
Same as above
Sample Input 3
[1, 2, 8, -1, 0, 3, 9]
[2, -1, 0, 11, 3]
false
The element 11 isn’t in the array, so the sequence array cannot be a subsequence / subset of the array
In your answer, please discuss your solution - what is its Big O Time & Space complexity? Why have you chosen this approach? Could there be a more efficient way (and if so, how)? 
If you are short on time, you can also submit pseudocode or simply describe what solution you’d write in code (just describe what you have in your mind) - this cannot attain full marks, but it is still a perfectly acceptable answer and can get partial marks. 
In essence, just submit what you have even if you don’t know the answer!

Algorithms 2 (Coding)
25 (1 question)
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.
The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
You may choose to submit a sorted approach, however the maximum marks this can attain is 10 marks. 
You can assume that there’ll always be at least one solution - there’ll always at least be a minimum of 3 numbers in the array, and you’ll always be able to return a smallest to largest array output.
For example, some sample input and outputs would be:

Array input
Output 
Why?
Sample Input 1
[141, 1, 17, -7, -27, 18, 541, 8, 7, 7]
[18, 141, 541]
Elements 18, 141 and 541 are the biggest three elements in the input array
Sample Input 2
[3, 1, 2]
[1, 2, 3]
Same logic as above
Sample Input 3
[142, 6, 34, 67, 31, -2, -5, 8]
[34, 67, 142]

Sample Input 4
[-4, 0, -2, -8, -142, -2, -8]
[-2, -2, 0]

In your answer, please discuss your solution - what is its Big O Time & Space complexity? Why have you chosen this approach? Could there be a more efficient way (and if so, how)? 
If you are short on time, you can also submit pseudocode or simply describe what solution you’d write in code (just describe what you have in your mind) - this cannot attain full marks, but it is still a perfectly acceptable answer and can get partial marks. 
In essence, just submit what you have even if you don’t know the answer!

## Concept Generation & Prototype (Design)
25 (1 question)
You have been tasked with creating a music application. When I (as a user) go onto this application, I should be able to select a desired song and listen to it.
You will not need to code anything, only design the application. As this is a vague and fairly open-ended question, consider the following points to include in your ‘design’ answer:
    • Consider - who is the user? Do they have a persona? Who are you catering for?
    • Design the application - what platform (web, mobile)? What may it look like (simple sketch is fine, or word-description)? What colours would you use and why? Think of this design like the way you approached the ‘Design the perfect door’ task for your Theory Assignment
    • What design heuristics and principles will you be following? How does your design meet or fail to meet them? 
    • What made you choose this design?
    • What are some future considerations you may need to make for your design? You can google for this question areas like “Future trends of UX / UI” (only this area - please).
    
#### ANSWER:

I like this question a lot :) I've been a user of quite several music websites, apps and forums for about 20 years now ^-^
• Consider - who is the user? Do they have a persona? Who are you catering for?
A varied customer base - I know for a fact people aged approximately 8 till 70 use such applications. They have different needs - teenagers love discovering new music similar to their tasates, and older generation seems to be much less keen on exploration. Last.fm had a nice set of tools for similar trend exploration, similar to Spotify. For older folks it's best to just give them a nice search tool, I think they'd welcome something like shazam a lot, as they might know the melody, but not the actual name of the artist or song. Ultimately everyone could benefit from all the abovementioned functions, just depending on user prowess - advanced user or not.
• Design the application - what platform (web, mobile)? What may it look like (simple sketch is fine, or word-description)? What colours would you use and why? Think of this design like the way you approached the ‘Design the perfect door’ task for your Theory Assignment.
No time for sketching, but if the main feature is supposed to be finding songs, not making playlists like with Spotify, then we should go with robust, obvious (in the middle) search - by artist, title, and put here also this "Shazam"alike function. Browse by genre should also be available - so all the search for nice music gimmicks I can think of. It can be presented in a nice minimalistic way, a bit like Google Search. Search bar and just options "search by what" - like with google image, just search by year, melody, artist, title, genre.
• What design heuristics and principles will you be following? How does your design meet or fail to meet them? 
Definitely I'd go with the most minimalistic approach to the search function as possible - 1 search bar, and it would be up to inside application logics to determine if the phrase is an artist, genre, year or title. The melody could be uploaded by drag and drop too. The simplier and more obvious the better.
• What made you choose this design?
Minimalism is the king! Perfection can only be achieved when there is nothing to detract anymore. Also, makes it more user friendly, time efficient for use, encouraging users to use the product because it doesn't obstruct what they want to do (find a song).
• What are some future considerations you may need to make for your design? You can google for this question areas like “Future trends of UX / UI” (only this area - please).
I'm not sure? I'd like a 1 page approach (SPA) to this, if this app is for music finding (main feature). Colours should be colorful but not anything neon like, too vibrant, too up in your face. 

    

