def binary_search(array, target):
	start = 0
	end = len(array)-1 
	while(start <=end):
		middle = start + int((end-start)/2)
		if(array[middle] == target):
			return middle 
		elif(array[middle] < target):
			start = middle + 1
		elif(array[middle] > target):
			end = middle -1
		else:
			return -1


def main():
    array = [13, 24, 30, 35, 44, 48, 59, 67, 71, 82, 89, 91, 108, 159, 201, 202]
    target = 108
    index = binary_search(array, target)
    if (index == -1):
        print("Element does not exist")
    else:
        print("Element is at index: ", index)


     




if __name__ == "__main__":
    main()