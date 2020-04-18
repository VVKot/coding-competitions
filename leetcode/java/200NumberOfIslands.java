import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
  private final int[] dRow = new int[] {1, 0, -1, 0};
  private final int[] dCol = new int[] {0, 1, 0, -1};

  public int numIslands(char[][] grid) {
    if (grid.length == 0) {
      return 0;
    }
    int islandsCount = 0;
    Set<Integer> visitedNodes = new HashSet<>();
    int rowCount = grid.length;
    int colCount = grid[0].length;
    for (int row = 0; row < rowCount; row++) {
      for (int col = 0; col < colCount; col++) {
        if (grid[row][col] != '1') {
          continue;
        }
        int nodeIdentifier = row * colCount + col;
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
          int currentRow = currentNode / colCount;
          int currentCol = currentNode % colCount;
          List<Integer> neighborNodes = getNeighborNodes(grid, currentRow, currentCol);
          for (int neighbor : neighborNodes) {
            if (!visitedNodes.contains(neighbor)) {
              nodesToVisit.offer(neighbor);
            }
          }
        }
      }
    }
    return islandsCount;
  }

  private List<Integer> getNeighborNodes(char[][] grid, int currentRow, int currentCol) {
    int rowCount = grid.length;
    int colCount = grid[0].length;
    List<Integer> neighborNodes = new ArrayList<>();
    for (int direction = 0; direction < 4; direction++) {
      int neighborRow = currentRow + dRow[direction];
      int neighborCol = currentCol + dCol[direction];
      int neighborId = neighborRow * colCount + neighborCol;
      if (neighborRow >= 0
          && neighborRow < rowCount
          && neighborCol >= 0
          && neighborCol < colCount
          && grid[neighborRow][neighborCol] == '1') {
        neighborNodes.add(neighborId);
      }
    }
    return neighborNodes;
  }
}
