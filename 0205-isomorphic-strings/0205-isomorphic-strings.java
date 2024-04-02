import java.util.Hashtable;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        Hashtable<Character, Character> sToT = new Hashtable<>();
        Hashtable<Character, Character> tToS = new Hashtable<>();
        
        for(int i=0; i<s.length();i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            
            
            
            if(sToT.containsKey(sChar)){
                if(sToT.get(sChar)!=tChar){
                    return false;
                }
            }
            else{
                  if(tToS.containsKey(tChar)){
                      return false;
                  }
                }
            
            sToT.put(sChar,tChar);
            tToS.put(tChar,sChar);         
            
        }
    
        
        return true;

    }
}