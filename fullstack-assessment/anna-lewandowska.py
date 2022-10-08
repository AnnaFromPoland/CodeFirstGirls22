# """
# Algorithms 1 Solution
# -------------------------------------------------------------------------------------------------------------------------
# """
# def isValidSubsequence(array, sequence):
#     pass

# # Some test cases are included in order to help you test your solution
# # Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# # As a result, make sure to think up some on your own and test your code as well!

# # Sample Tests for Algorithms 1
# # ---------------------------------------------------------

# array1 = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence1 = [1, 6, -1, -2]

# array2 = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence2 = [1, 6, -1, 10]

# array3 = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence3 = [25]


def isValidSubsequence(array, sequence):
    for number in sequence:
        if number not in array:
            return False
    return True


# print(isValidSubsequence(array1, sequence1))  # FALSE
# print(isValidSubsequence(array2, sequence2))  # TRUE
# print(isValidSubsequence(array3, sequence3))  # TRUE


# Talking about this solution: It just checks it the numbers are in the sequence given. It's a very simple solution, a
# simplistic one even - I made this choice because of short time given for this exam. If numbers are in the original
# sequence, the answer is true. If not, it's false.


# """
# Algorithms 2 Solution
# -------------------------------------------------------------------------------------------------------------------------
# """
# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!



# # Sample Tests for Algorithms 2
# # ---------------------------------------------------------
#
# expectedOutput = []
# array1 = [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
#
# # array1 = [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
# # expectedOutput1 = [18, 141, 541]
# # print(str(findThreeLargestNumbers(array1)) + " <-- --> " + str(expectedOutput1))  # [18, 141, 541]
#
# # array2 = [141, 1, 214, -17, -27, 0, 541, 21, 7, 34]
# # expectedOutput2 = [141, 214, 541]
# # print(str(findThreeLargestNumbers(array2)) + " <-- --> " + str(expectedOutput2))  # [141, 214, 541]
#
#
# def findThreeLargestNumbers(array1):
#     for i in range(3):
#         temp_max = array1[0]
#         for x in array1:
#             if x > temp_max:
#                 temp_max = x
#         popped = array1.pop(array1.index(temp_max))
#         expectedOutput_unsorted.append(popped)
#
#
# print(str(findThreeLargestNumbers(array1)) + " <-- --> " + str(expectedOutput))
#
#
# Talking about this solution: It's not the best because it doesn't sort. At first I've tried sorting as well but I
# got wrong results. I have a semblance of an idea why, but I don't have time for trial and error now. This gives 3
# correct results, but not sorted. Sorting would take another precious while and this exam is only so short. I am
# sadly not good enough yet to write this up in a very short while. It may also have hiccups with equal numbers
# (two tens) but I did not have any quick ideas how to approach it.
