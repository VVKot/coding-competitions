import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class Solution {
  public int numIslands(char[][] grid) {
    if (grid.length == 0) {
      return 0;
    }
    int islandsCount = 0;
    int[] dr = new int[] {1, 0, -1, 0};
    int[] dc = new int[] {0, 1, 0, -1};
    Set<Integer> visitedNodes = new HashSet<>();
    int rowsCount = grid.length;
    int colsCount = grid[0].length;
    for (int row = 0; row < rowsCount; row++) {
      for (int col = 0; col < colsCount; col++) {
        if (grid[row][col] != '1') {
          continue;
        }
        int nodeIdentifier = row * colsCount + col;
        if (visitedNodes.contains(nodeIdentifier)) {
          continue;
        }
        islandsCount++;
        Deque<Integer> nodesToVisit = new ArrayDeque<Integer>();
        nodesToVisit.offer(nodeIdentifier);
        while (!nodesToVisit.isEmpty()) {
          int currentNode = nodesToVisit.poll();
          if (visitedNodes.contains(currentNode)) {
            continue;
          }
          visitedNodes.add(currentNode);
          int currentRow = currentNode / colsCount;
          int currentCol = currentNode % colsCount;
          for (int direction = 0; direction < 4; direction++) {
            int neighborRow = currentRow + dr[direction];
            int neighborCol = currentCol + dc[direction];
            int neighborId = neighborRow * colsCount + neighborCol;
            if (neighborRow >= 0
                && neighborRow < rowsCount
                && neighborCol >= 0
                && neighborCol < colsCount
                && grid[neighborRow][neighborCol] == '1'
                && !visitedNodes.contains(neighborId)) {
              nodesToVisit.offer(neighborId);
            }
          }
        }
      }
    }
    return islandsCount;
  }
}
