class Solution {
    public int findMaxK(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        Arrays.sort(nums);
        
        while(end >= 0 && nums[end] >0 ){
            if (-nums[start] == nums[end]){
                return nums[end];
            }
            if(nums[start] > 0){
                start = 0;
                end--;
            }else{
            start++;
            }
            
        }
            
            
            
        return -1;
    }
}