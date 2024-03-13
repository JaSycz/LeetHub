import java.util.Enumeration;
import java.util.Hashtable;


class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
      Hashtable<String,List<String>>  tb = new Hashtable<>();  
        for(String str:strs){
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);
            List<String> list = tb.get(sortedString);
            if(list == null){
                list = new ArrayList<>();
                list.add(str);
                tb.put(sortedString,list);
            }
            else{
            list.add(str);
            tb.put(sortedString,list);
            }
        }
        Enumeration<String> keys = tb.keys();
        List<List<String>> l = new ArrayList<List<String>>();
        while (keys.hasMoreElements()) {
            String key = keys.nextElement();
            l.add(tb.get(key));
        }
        return l;
    }
}
       