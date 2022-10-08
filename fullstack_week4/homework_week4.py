# Two Sum
# -------------------------------------------------------------------------------------------------------------------------
# Given an array of integers numbers and an integer target, return two numbers from inside that array such that they
# add up to the target. You may assume that each input would have at least one solution, and you may not use the same
# element twice. You can return the answer in any order.
#
# EXAMPLE 1:
# ---------------------------------------------------------------
# Input: nums = [2,7,11,15], target = 9
# Output: [2, 7]
# Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].
#
# EXAMPLE 2:
# ---------------------------------------------------------------
# Input: nums = [3,2,4], target = 6
# Output: [2, 4]
#
# EXAMPLE 3:
# ---------------------------------------------------------------
# Input: nums = [3,3], target = 6
# Output: [3, 3]
#
# NOTES:
# ---------------------------------------------------------------
# - An input MAY HAVE no two numbers at all (an empty one) in which case, return an empty array
# - It's an array of integer numbers - these numbers are not necessarily distinct / unique
# - Make sure to discuss your solution - what is the Big O Time & Space complexity? Was there anyway you could've done
# better or not? Why or why not? Justify.

# input an array of numbers, any will do
numbers_array = [4, 5, 8, 12, 43, 21, 34, 54, 66, 7, 21]
# input the target number (target of the sum)
target_number = 9


def twoSum(numbers, target):
    output = []
    # if array is empty, return empty array immediately
    if len(numbers) != 0:
        # first loop goes ltr increments by +1 till finds number <= than target
        for i in range(len(numbers)):
            if numbers[i] <= target:
                # second loop goes ltr from next index item after ^ found number
                for j in range(i+1, len(numbers)):
                    # looking for a number <= than target
                    if numbers[j] <= target:
                        # which also gives sum == target with our 1st number found
                        if numbers[i] + numbers[j] == target:
                            output.append(numbers[i])
                            output.append(numbers[j])
                            return output
    return output


print(twoSum(numbers_array, target_number))

# about my solution
# this solution is of course not perfect, because it basically matches 1st found number which *could* be one of a pair
# adding up to a certain target sum and then looks in the remainder of the array for a matching pair for it - this means
# other pairs in the same array meeting our condition (two numbers adding to sum target number) could exist in our array
# but we might never know and find them out.
# however, it'd be rather easy to create a simple piece of code which would compare each array item with each another
# array item to check for ALL possible pairs meeting out condition. i understood the "each element can be only accessed
# once as a challenge in code / algorightm optimalisation. first i wrote a regular loop, then a loop which went from
# both left and right and met in the middle, this met the condition of "each element can be accessed only once" but it
# had the possibility of omitting an array item (if its not symmetrical) and also of missing pairs just because of array
# item ordering (so both a and b summing up to target sum c could exist, but due to incremental nature and only
# comparing 2 numbers at 1 time and then never returning to them, if the 2 being compared would not be a match, a pair
# might not have been found using this way.
# this function is even optimised in the way it does not bother with certain conditions rendering numbers irrelevant to
# it - if array is empty, no logic is performed. if number is greater than target sum number, then such numbers are also
# omitted, since we are told we'll be dealing with arrays of only natural numbers, full integers, so numbers bigger than
# the target-sum-number are excluded as they'd need to be summed with a negative number to give the target sum number as
# the result. maybe it was arbitrary from me to not think of negative numbers, but that's an assumption i made, that the
# arrays will have only natural positive full integer numbers. the task did not describe otherwise.
# this function deals with arrays of any size too, so it's reusable.
# the plus of my solution is that it adheres to the 1 time access for each item only rule, so it's not too costly in
# terms of time or resources - should be an easy O(n+n).
# the minus of my solution is that more pairs could exist, but since my algorithm catches the 1st number meeting the
# condition and looks for a second one, only 1 pair or no pairs could be found. for example, if we catch 9 and target is
# 9 and there is no 0 in the remaining numbers, there won't be any pair. that's a weakness. if we catch 8 with target 9
# the remainder items in array must contain 1 in order for this function to return pair 8 + 1 = 9.
# i think it should be possible to write a huge function which would write each element meeting our condition down in a
# separate array (so if target is 9, it would write down any number from 0-9) and then spit up all the pairs, which
# technically would be accessing each array item only once (cause we'd write it down in temporary separate array) but to
# me that seemed excessive, unnecessary and too bulky, not cost-efficient - with bigger arrays the cost of operating on
# great many array items in such way would grow logarithmically not simply O(n + n) like here in case of my array.

