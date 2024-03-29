class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer > table = new HashMap<>();
        int[] twoIndices = new int[2];
        for(int i=0;i<nums.length; i++){
            if(table.containsKey(nums[i])){
                twoIndices[0] = i;
                twoIndices[1] = table.get(nums[i]);
                break;
            }
            else{
                table.put(target-nums[i],i);
            }
        }
        return twoIndices;
        
    }
}