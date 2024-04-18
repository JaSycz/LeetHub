class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[i].length; j++){
                if(grid[i][j] == 1){
                    if(i-1 < 0) perimeter++;
                    else if(grid[i-1][j] == 0) perimeter++;
                    
                    if(i+1 > grid.length - 1) perimeter++;
                    else if(grid[i+1][j] == 0) perimeter++;
                    
                    if(j+1 > grid[i].length - 1) perimeter++;
                    else if(grid[i][j+1] == 0) perimeter++;
                    
                    if(j-1 < 0) perimeter++;
                    else if(grid[i][j-1] == 0) perimeter++;
                    
            
                    
                }
            }
        }
        return perimeter;
    }
}