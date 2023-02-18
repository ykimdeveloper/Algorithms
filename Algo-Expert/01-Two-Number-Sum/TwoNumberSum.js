/*
Write a function that takes in a non-empty array of distinct integers and an 
integer representing a target sum. If any two numbers in the input array sum 
up to the target sum, the function should return them in an array, in sorted order. 
If no two numbers sum up to the target sum, the function should return an empty array. 
Assume that there will be at most one pair of numbers summing up to the target sum.

Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 
Sample output:[-1, 11]

*/

const twoSum = (arr, target) =>{
    let storage = {};
    for (const [key, value] of arr.entries()){
        temp = target - value
        if(Object.values(storage).includes(temp) && target == temp + value){
            return [arr[key], temp]
        }else{
            storage[key] = value
        }
    }
}




const arr = [3, 5, -4, 8, 11, 1, -1, 6];
const target = 10;

const val = twoSum(arr, target)
console.log(val)