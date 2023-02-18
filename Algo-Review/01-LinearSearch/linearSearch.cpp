#include<stdio.h>
#include<iostream>
#define SIZE 7
int LinearSearch(int arr[], int size, int key)
{
    int i;
    for(i = 0; i < size; i++)
        if(arr[i] == key)
            return i; 
        return -1;
}

int main()
{
    int page_number[SIZE] = {53, 13, 64, 34, 12, 63, 53};
    int key = 34;
    int index = LinearSearch(page_number, SIZE,key);
    if(index != -1){
       printf("\nElement at index " + index);

    }
    else
        printf("\nSearch Not Found\n");
    return 0;
}