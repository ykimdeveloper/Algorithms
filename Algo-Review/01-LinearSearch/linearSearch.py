def linearSearch(arr, val):
    for i in range(0, len(arr)):
        if arr[i] == val:
            return i 
    return -1
  
def main():
    arr = [53, 13, 64, 34, 12, 63, 91]
    val = 34
    index = linearSearch(arr, val)
    if (index != -1):
        print('Element found at index ', index)
    else:
        print('Element not found ')
     

if __name__ == "__main__":
    main()