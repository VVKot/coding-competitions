import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
  private final int[] dRow = new int[] {1, 0, -1, 0};
  private final int[] dCol = new int[] {0, 1, 0, -1};

  public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
    int startingColor = image[sr][sc];
    if (image[sr][sc] == newColor) {
      return image;
    }
    int cols = image[0].length;
    Queue<Integer> nodesToProcess = new ArrayDeque<>();
    nodesToProcess.offer(sr * cols + sc);
    while (!nodesToProcess.isEmpty()) {
      int currentNode = nodesToProcess.poll();
      int currentRow = currentNode / cols;
      int currentCol = currentNode % cols;
      image[currentRow][currentCol] = newColor;
      List<Integer> neighborNodes = getNeighborNodes(image, currentRow, currentCol, startingColor);
      for (int neighbor : neighborNodes) {
        nodesToProcess.offer(neighbor);
      }
    }
    return image;
  }

  private List<Integer> getNeighborNodes(
      int[][] grid, int currentRow, int currentCol, int targetColor) {
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
          && grid[neighborRow][neighborCol] == targetColor) {
        neighborNodes.add(neighborId);
      }
    }
    return neighborNodes;
  }
}
