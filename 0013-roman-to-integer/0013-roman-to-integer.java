import java.util.Hashtable;

class Solution {
    public int romanToInt(String s) {
        Hashtable<Character,Integer> romanToDecimal = new Hashtable<>(); 
        romanToDecimal.put('I',1);
        romanToDecimal.put('V',5);
        romanToDecimal.put('X',10);
        romanToDecimal.put('L',50);
        romanToDecimal.put('C',100);
        romanToDecimal.put('D',500);
        romanToDecimal.put('M',1000);
        int decimal=0;
        
        for(int i=0; i<s.length();i++){
            
            if( i < s.length() -1 && romanToDecimal.get((s.charAt(i))) < romanToDecimal.get((s.charAt(i+1)))){
                
                decimal -= romanToDecimal.get((s.charAt(i)));
            } else {
                decimal += romanToDecimal.get((s.charAt(i)));
            }

       
        }
         return decimal;        
    }
}