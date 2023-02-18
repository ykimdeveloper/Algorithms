#Write a function that takes in a non-empty array of distinct integers and an 
# integer representing a target sum. If any two numbers in the input array sum 
# up to the target sum, the function should return them in an array, in sorted order. 
# If no two numbers sum up to the target sum, the function should return an empty array. 
# Assume that there will be at most one pair of numbers summing up to the target sum.

# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 
# Sample output:[-1, 11]

# {3: True, 5: True, -4 : True, 8 : True, 11 : True, 1 : True, 1 : True, -1 : True}
# {3: True, 5: True, -4 : True, 8 : True, 11 : False, 1 : True, 1 : True, -1 : False}


def twoSum(target, array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)-1):
            if array[i]+array[j] == target:
                return array[i], array[j]


def main():
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    val1, val2, = twoSum(target, arr)
    print(str(val1) + " " + str(val2))


if __name__ == "__main__":
    main() 