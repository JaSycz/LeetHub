class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        int n  = result.length;    
        for(int i=0; i < n; i++){
            result[i] = 1;
        }
        
        int prefix  = 1;
        
        for(int i=0; i < n; i++){
            result[i] *= prefix;
            prefix *= nums[i];
        }
        prefix = 1;
        for(int i=n - 1; i >= 0; i--){
            result[i] *= prefix;
            prefix *= nums[i];
        }
        
        return result;
    }
}