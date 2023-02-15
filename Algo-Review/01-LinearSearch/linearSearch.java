public class linearSearch{
    public static void main(String args[]){
        int[] array = {53, 13, 64, 34, 12, 63, 53};
        int index = linear_search(array, 34);

        if(index != -1){
            System.out.println("Element found at index: " + index);
        }
        else {
            System.out.println("Element not found");
        }
    }

    private static int linear_search(int[] array, int value){
        for(int i = 0; i<array.length; i++){
            if(array[i]==value){
                return i;
            }
        }
        return -1;
    }
}