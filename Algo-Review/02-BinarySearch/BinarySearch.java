public class BinarySearch {
    public static void main(String args[]){
        int[] array = {13, 24, 30, 35, 44, 48, 59, 67, 71, 82, 89, 91, 108, 159, 201};
        int target = 91;
        int index = binary_search(array, target);

        if( index == -1){
            System.out.println(target + " not found");
        }
        else{
            System.out.println("Element "+ target + " at index " + index);
        }
    }

    private static int binary_search(int[] array, int target){
        int low = 0;
        int high = array.length -1;

        while(low <= high){
            int middle = low + (high-low)/2;
            int value = array[middle];

            // if(value < target){
            //     low = middle + 1;
            // }
            // else if(value > target){
            //     high = middle - 1;
            // }
            // else{
            //     return middle;
            // }

            if(value < target) low = middle + 1;
            else if(value > target) high = middle - 1;
            else return middle;
            
        }
        return -1;
    }
}

