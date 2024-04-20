class Solution {
    public int[][] findFarmland(int[][] land) {
        List<int[]> groups = new ArrayList<>();
        int[] group = new int[4];
        for(int i = 0; i < land.length; i++){
            for(int j = 0; j< land[i].length; j++){
                if(land[i][j] == 1){
                    groupSearch(land,group,i,j);
                    groups.add(group);
                    group = new int[4];
                }
            }
        }
        
        
    return groups.stream().toArray(int[][] :: new);
    }

    public void groupSearch(int[][]land, int[] group,int i, int j){
        if(i >= land.length || i < 0 || j >= land[i].length || j < 0 || land[i][j] != 1 ) return; 
        if ( (i - 1 < 0 || land[i-1][j] == 0) && (j - 1 < 0 || land[i][j-1] == 0)){ 
            group[0] = i;
            group[1] = j;
        }
        if((i + 1 >= land.length || land[i+1][j] == 0)  && (j + 1 >= land[0].length || land[i][j+1] == 0)){
            group[2] = i;
            group[3] = j;
        }
        land[i][j] = -1;
        groupSearch(land,group,i-1,j);
        groupSearch(land,group,i,j-1);
        groupSearch(land,group,i+1,j);
        groupSearch(land,group,i,j+1);

    }
}