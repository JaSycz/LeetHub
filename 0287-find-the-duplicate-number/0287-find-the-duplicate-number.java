class Solution {
    public int findDuplicate(int[] nums) {
        boolean[] isDup = new boolean[nums.length];
        
        for(int i=0;i<nums.length;i++){
            if(isDup[nums[i]-1]){
                return nums[i];
            }
            isDup[nums[i]-1] = true;
        }
        return -1;
    }
}