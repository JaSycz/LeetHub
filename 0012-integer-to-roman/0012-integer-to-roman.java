class Solution {
    public String intToRoman(int num) {
        StringBuilder ans = new StringBuilder();
        int numDiv = num;
        int sub = num/1000;
        int j;
        for(int i=0; i < sub; i++){
            ans.append("M");
        }
        numDiv = num - sub*1000;
        sub  = numDiv/100;
        j = sub;
        while(j!=0){
            if(j/9!=0){
                ans.append("CM");
                j = j- (j/9)*9;
            }
            else if(j/5!=0){
                ans.append("D");
                j = j - (j/5)*5;
            }
            else if(j/4!=0){
                ans.append("CD");
                j = j - (j/4)*4;
            }
            else{
                ans.append("C");
                j--;
            }

        }
        numDiv = numDiv - sub*100;
        sub  = numDiv/10;
        j = sub;
        while(j!=0){
            if(j/9!=0){
                ans.append("XC");
                j = j- (j/9)*9;
            }
            else if(j/5!=0){
                ans.append("L");
                j = j - (j/5)*5;
            }
            else if(j/4!=0){
                ans.append("XL");
                j = j - (j/4)*4;
            }
            else{
                ans.append("X");
                j--;
            }
        }
        numDiv = numDiv - sub*10;
        j = numDiv;
        while(j!=0){
            if(j/9!=0){
                ans.append("IX");
                j = j- (j/9)*9;
            }
            else if(j/5!=0){
                ans.append("V");
                j = j - (j/5)*5;
            }
            else if(j/4!=0){
                ans.append("IV");
                j = j - (j/4)*4;
            }
            else{
                ans.append("I");
                j--;
            }
        }
        return ans.toString();
        
        
        

    }
}