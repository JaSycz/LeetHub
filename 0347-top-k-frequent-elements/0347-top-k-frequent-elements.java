import java.util.*;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Hashtable<Integer,Integer> tb = new Hashtable<>();
        for(int num:nums){

            tb.put(num,tb.getOrDefault(num,0)+1); 
        }
        
        List<Integer>list=new ArrayList<>(tb.keySet());
        list.sort((a, b) -> tb.get(b) - tb.get(a));
        int res[] = new int[k];
        for (int i = 0; i < k; ++i)
            res[i] = list.get(i);
	return res;

        
    
        
    }
}


