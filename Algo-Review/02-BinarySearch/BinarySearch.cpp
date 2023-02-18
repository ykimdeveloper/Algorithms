#include<stdio.h>
#define SIZE 15
int binarySearch(int array[], int target)
{
    int low = 0;
    int high = SIZE;
    while(low <= high){
        int middle = low + (high - low)/2;
        int value = array[middle];
        if(value <  target){
            low = middle + 1;
        }
        else if(value > target){
            high = middle - 1;
        }
        else{
            printf("middle: " + middle);
            return middle;
        }

    }

    return -1;
}

int main()
{
    int target = 91;
    int array[SIZE] = {13, 24, 30, 35, 44, 48, 59, 67, 71, 82, 89, 91, 108, 159, 201};
    int index = binarySearch(array, target);
    if ( index == -1){
        printf(target + " not found");
    } 
    else {
        printf("\nElement is at index " + index);
        printf("\n\n\n");
    }
}