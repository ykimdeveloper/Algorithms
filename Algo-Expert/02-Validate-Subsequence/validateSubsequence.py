# Q: Given two non-empty arrays of integers, write a function that determines whether 
#the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent in 
#the array but that are in the same order as they appear in the array. 
#For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], 
#and so do the numbers [2, 4]. Noe that a single number in an array and the array 
#itself are both valid subsequences of the array.

# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Sample Output
# true

#Time complexity: O(n) as n is the length of the array
#Space complexity: O(1) b/c using only constant space 

def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0 
    
    while(arrIdx < len(array) and seqIdx < len(sequence)):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx +=1
        else:
            arrIdx +=1
        if len(sequence)==seqIdx:
            return True 
    return False

def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))  






if __name__ == "__main__":
    main()