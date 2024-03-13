class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sCharArr = s.toCharArray();
        char[] tCharArr = t.toCharArray();
        Arrays.sort(sCharArr);
        Arrays.sort(tCharArr);
        String sSorted = new String(sCharArr);
        String tSorted = new String(tCharArr);
        if(sSorted.equals(tSorted)){
            return true;
        }
        return false;
    }
}