class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i,j;
        i=0;
        j=numbers.length-1;
        int[] twoIndices = new int[2];
        while(i < numbers.length && j >= 0){
            if( numbers[i] + numbers[j] == target ){
                twoIndices[0] = i+1;
                twoIndices[1] = j+1; 
                break;
            }
            else if( numbers[i]+numbers[j] > target){
                j--;
            }
            else if( numbers[i]+numbers[j] < target){
                i++;
            }
        }
        return twoIndices;
        
    }
}