class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> numbers = new HashSet<>();
        
        for(int i=0;i<nums.length;i++){
            if(!numbers.contains(nums[i])){
                numbers.add(nums[i]);
            }
            else{
                return nums[i];
            }
        }
        return -1;
    }
}