class Solution {
    public boolean isValidSudoku(char[][] board) {
        int columns=9,rows=9;
        HashSet<Character> set = new HashSet<>();
        for(int row=0;row<rows;row++){
            for(int col=0;col<columns;col++){
                if(board[row][col]!='.' && set.contains(board[row][col])){
                    return false;
                }
                set.add(board[row][col]);
            }
            set.clear();
        }
        
        for(int col=0;col<columns;col++){
            for(int row=0;row<rows;row++){
                if(board[row][col]!='.' && set.contains(board[row][col])){
                    return false;
                }
                set.add(board[row][col]);
            }
            set.clear();
        }
        
        int n=0;
        while(n<9){
            for(int row=0;row<9;row++){
                if(row%3==0){
                    set.clear();
                }
                for(int col=n;col<n+3;col++){
                    if(board[row][col]!='.' && set.contains(board[row][col])){
                        return false;
                        }
                    set.add(board[row][col]);
                }
            }
           n+=3;
              
        }

        return true;
    }
}