class Solution {
    public boolean isPalindrome(String s) {
        String alphaStr = s.trim().toLowerCase().replaceAll("[^a-z0-9]","");
        char[] alphaCharArr = alphaStr.toCharArray();
        int start,end;
        start = 0;
        end = alphaCharArr.length -1;
        while(start < end){
            if(alphaCharArr[start] != alphaCharArr[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}