import java.util.Arrays;
class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        HashSet<Integer> set = new HashSet<>();
        int prev=0,count=1,max=0;
        if(nums.length>0){
            set.add(1);
        }
        for(int i=1;i<nums.length;i++){
            if(nums[prev]+1 == nums[i]){
                count++;
            }else if(nums[prev]==nums[i]){
                
            }else{
                count=1;
            }
            set.add(count);
            prev=i;
        }
        
        for(int num:set){
            if(max<num){
                max=num;
            }
            
        }
        return max;
        
        
        
}
}


