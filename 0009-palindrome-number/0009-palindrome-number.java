class Solution {
    public boolean isPalindrome(int x) {
        String num  = String.valueOf(x);
        int length = num.length();
        for(int i=0;i<length/2;i++){
            if(num.charAt(i)!=num.charAt(length-1-i)){
                return false;
            }
        }
        return true;
        
        
    }
}
