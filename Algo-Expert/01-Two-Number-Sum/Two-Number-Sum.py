#Write a function that takes in a non-empty array of distinct integers and an 
# integer representing a target sum. If any two numbers in the input array sum 
# up to the target sum, the function should return them in an array, in sorted order. 
# If no two numbers sum up to the target sum, the function should return an empty array. 
# Assume that there will be at most one pair of numbers summing up to the target sum.

# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 
# Sample output:[-1, 11]


#brute force
# O(n^2) time & O(1)space
def twoSumBF(target, array):
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == target:
                return [array[i], array[j]]
    return []

#hash table
# O(n) time & O(n) space
def twoSumHT(target, array):
    storage = {}
    for i in range(0, len(array)-1):
        temp = target - array[i]
        if temp in storage and (target == temp + array[i]):
            return [temp, array[i]]
        else:
            storage[array[i]] = i
    return []

def main():
    arr = [3, 5, -4, 8, 11, 1, -1, 6]
    target = 10
    twosumbf = twoSumBF(target, arr)
    print(twosumbf)
    twosumht= twoSumHT(target, arr)
    print(twosumht)




if __name__ == "__main__":
    main() 