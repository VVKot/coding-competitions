/**
 * T: O(R*C) S: O(R*C)
 *
 * <p>Find all rotten oranges, iterate over all of their neighbors that will rot and remember their
 * rot time. If after that there are still fresh oranges - return -1; otherwise return maximum seen
 * rot time(if any).
 */
import java.util.ArrayDeque;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Queue;

class Solution {
  int EMPTY_CELL = 0;
  int FRESH_ORANGE = 1;
  int ROTTEN_ORANGE = 2;
  int[] dx = new int[] {-1, 0, 1, 0};
  int[] dy = new int[] {0, -1, 0, 1};

  public int orangesRotting(int[][] grid) {
    int rows = grid.length;
    int cols = grid[0].length;
    Queue<Integer> rottenOranges = new ArrayDeque<>() {};
    Map<Integer, Integer> depth = new HashMap<>();
    for (int y = 0; y < rows; y++) {
      for (int x = 0; x < cols; x++) {
        if (grid[y][x] == ROTTEN_ORANGE) {
          int cellCode = y * cols + x;
          rottenOranges.offer(cellCode);
          depth.put(cellCode, 0);
        }
      }
    }
    while (!rottenOranges.isEmpty()) {
      int currentCellCode = rottenOranges.poll();
      int currentY = currentCellCode / cols;
      int currentX = currentCellCode % cols;
      for (int direction = 0; direction < dx.length; direction++) {
        int nextY = currentY + dy[direction];
        int nextX = currentX + dx[direction];
        if (nextY >= 0
            && nextY < rows
            && nextX >= 0
            && nextX < cols
            && grid[nextY][nextX] == FRESH_ORANGE) {
          grid[nextY][nextX] = ROTTEN_ORANGE;
          int nextCellCode = nextY * cols + nextX;
          rottenOranges.offer(nextCellCode);
          depth.put(nextCellCode, depth.get(currentCellCode) + 1);
        }
      }
    }
    for (int[] row : grid) {
      for (int cell : row) {
        if (cell == FRESH_ORANGE) {
          return -1;
        }
      }
    }
    return depth.size() == 0 ? 0 : Collections.max(depth.values());
  }
}
