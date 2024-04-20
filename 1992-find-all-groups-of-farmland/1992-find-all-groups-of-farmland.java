class Solution {
    public int[][] findFarmland(int[][] land) {
        int[][] groups = new int[land.length*land[0].length][4];
        int group = 0;
        for(int i = 0; i < land.length; i++){
            for(int j = 0; j< land[i].length; j++){
                if(land[i][j] == 1){
                    groupSearch(land,groups,i,j,group);
                    group++;
                }
            }
        }
        int groupsFixed[][] = new int[group][4];
        for(int k = 0; k < group; k++){
            groupsFixed[k] = groups[k]; 
        }
        return groupsFixed;
    }

    public void groupSearch(int[][]land, int[][] groups,int i, int j,int group){
        if(i >= land.length || i < 0 || j >= land[i].length || j < 0 || land[i][j] != 1 ) return; 
        if ( (i - 1 < 0 || land[i-1][j] == 0) && (j - 1 < 0 || land[i][j-1] == 0)){ 
            groups[group][0] = i;
            groups[group][1] = j;
        }
        if((i + 1 >= land.length || land[i+1][j] == 0)  && (j + 1 >= land[0].length || land[i][j+1] == 0)){
            groups[group][2] = i;
            groups[group][3] = j;
        }
        land[i][j] = -1;
        groupSearch(land,groups,i-1,j,group);
        groupSearch(land,groups,i,j-1,group);
        groupSearch(land,groups,i+1,j,group);
        groupSearch(land,groups,i,j+1,group);

    }
}