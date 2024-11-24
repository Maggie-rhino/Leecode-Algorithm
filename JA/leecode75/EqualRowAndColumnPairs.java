package JA.leecode75;


public class EqualRowAndColumnPairs {

    // Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
    // Output: 1
    // Explanation: There is 1 equal row and column pair:
    // - (Row 2, Column 1): [2,7,7]

    // Constraints:
    // n == grid.length == grid[i].length
    // 1 <= n <= 200
    // 1 <= grid[i][j] <= 105

    public int equalPairs(int[][] grid) {
        // first, hash every row and column
        // create  two nested arrays, one for rows and one for columns, to storage the hash value;
        //  then iterate the each value of the row, and compare with that in the column, and count the pairs
        String[] rowHash = new String[grid.length];
        String[] colHash = new String[grid[0].length];

        for(int i =0;i<grid.length;i++){
            int[] row =grid[i];
            for(int r:row){rowHash[i] +="+"+Integer.toString(r);}
        }
        for(int j =0;j<grid[0].length;j++){
            int[] colValues = new int[grid.length];
            for (int idx =0;idx< grid.length;idx++){
                colValues[idx] = grid[idx][j];
            }
            for(int v:colValues){colHash[j] +="+"+Integer.toString(v);}
        }
        int pairs =0;
        for(String rowV: rowHash){
            for(String colV: colHash){
                if (rowV.equals(colV)){pairs++;}
            }
        }
        return pairs;
    }



    public static void main(String[] args) {
        int[][] grid = {{2,1},{3,32}};
        EqualRowAndColumnPairs solution = new EqualRowAndColumnPairs();
        System.out.println(solution.equalPairs(grid));
    }
}
