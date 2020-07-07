class Solution {

    private final int LAND = 1;
    private final int EDGES_PER_CELL = 4;
    private final int EDGES_PER_NEIGHBOR_CONNECTION = 2;

    public int islandPerimeter(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int result = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == LAND) {
                    result += EDGES_PER_CELL;
                    
                    if (r > 0 && grid[r-1][c] == LAND) {
                        result -= EDGES_PER_NEIGHBOR_CONNECTION;
                    }
                    
                    if (c > 0 && grid[r][c-1] == LAND) {
                        result -= EDGES_PER_NEIGHBOR_CONNECTION;
                    }
                }
            }
        }
        
        return result;
    }
}
