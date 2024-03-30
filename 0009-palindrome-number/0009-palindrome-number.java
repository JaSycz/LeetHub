class Solution {
    public boolean isPalindrome(int x) {
        String num  = String.valueOf(x);
        int end = num.length()-1;
        int start = 0;
        while(start<end){
            if(num.charAt(start)!=num.charAt(end)){
                return false;
            }
            start++;
            end--;
        }
        return true;
        
        
    }
}
