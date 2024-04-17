class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = new int[nums1.length+nums2.length];
        int i = 0, j = 0 , mn = 0;
        while(i< nums1.length){
            merged[mn++] = nums1[i++];
            
        }
        while(j < nums2.length){
            merged[mn++] = nums2[j++];
        }
        
        Arrays.sort(merged);
        
        if(merged.length%2 == 0){
            double median = (double)(merged[merged.length/2] + merged[(merged.length/2) - 1]) /2; 
            return median;
        }else{
            
            return merged[merged.length/2];
        }
        
        
        
    }
}