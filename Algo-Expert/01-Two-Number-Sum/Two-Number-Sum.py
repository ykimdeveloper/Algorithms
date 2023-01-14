#Write a function that takes in a non-empty array of distinct integers and an 
# integer representing a target sum. If any two numbers in the input array sum 
# up to the target sum, the function should return them in an array, in sorted order. 
# If no two numbers sum up to the target sum, the function should return an empty array. 
# Assume that there will be at most one pair of numbers summing up to the target sum.

# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 
# Sample output:[-1, 11]

# {3: True, 5: True, -4 : True, 8 : True, 11 : True, 1 : True, 1 : True, -1 : True}
# {3: True, 5: True, -4 : True, 8 : True, 11 : False, 1 : True, 1 : True, -1 : False}