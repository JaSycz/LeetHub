class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] productsWithouti= new int[nums.length];
        int product=1;
        int productIfZero=1;
        for(int num:nums){
            product*=num;
            
        }
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                for(int k=i+1; k<nums.length; k++){
                    productIfZero*=nums[k];
                }
                for(int j=i-1; j>=0; j--){
                    productIfZero*=nums[j];
                }
                productsWithouti[i]=productIfZero;
            }
            else{
            productsWithouti[i]=(product/nums[i]);
            }
        }
        return productsWithouti;
    }
}