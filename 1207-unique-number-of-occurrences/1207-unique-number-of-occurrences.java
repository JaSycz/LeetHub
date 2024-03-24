import java.util.Hashtable;
import java.util.HashSet;
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Hashtable<Integer,Integer> numOfOcc = new Hashtable<>();
        HashSet<Integer> uniqOcc = new HashSet<Integer>(); 
        int lenght = arr.length;
        
        for (int i : arr) {
            numOfOcc.put(i, numOfOcc.getOrDefault(i, 0) + 1);
        }

        for(int count :numOfOcc.values()){
            if(!uniqOcc.add(count)){
                return false;
            }                      
        }
        return true;
    }
}