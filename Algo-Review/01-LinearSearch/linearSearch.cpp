#include<stdio.h>
#define SIZE 7
int LinearSearch(int arr[], int size, int key)
{
    int i;
    for(i = 0; i < size; i++)
        if(arr[i] == key)
            return 1; 
        return 0;
}

int main()
{
    int page_number[SIZE] = {53, 13, 64, 34, 12, 63, 53};
    int key = 34;
    if(LinearSearch(page_number, SIZE,key) == 1)
        printf("Search Found\n");
    else
        printf("Search Not Found\n");
    return 0;
}