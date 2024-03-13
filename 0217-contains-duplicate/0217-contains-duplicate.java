class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int i,j;
        i = 0;
        while (i < nums.length-1){
            j = i+1;
            if ( nums[i] ==  nums[j]){
                return true;
            }
            i++;
        }
        return false;
    }
}
