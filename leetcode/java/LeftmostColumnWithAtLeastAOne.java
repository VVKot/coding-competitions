/**
 * T: O(N+M) S: O(1)
 *
 * <p>Start in the top right corner, inspect the nodes as we go. If node has 1 in it - we have to go
 * left, if it is a zero - we should start inspecting next row from the same column. There is no
 * need to inspect the columns to the right of the current one in any subsequent rows since we
 * already found a column to the left of them.
 */
import java.util.List;

interface BinaryMatrix {
  public int get(int x, int y);

  public List<Integer> dimensions();
};

class Solution {
  public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
    List<Integer> dimensions = binaryMatrix.dimensions();
    int rows = dimensions.get(0);
    int cols = dimensions.get(1);
    int currentRow = 0;
    int currentCol = cols - 1;
    while (currentRow < rows && currentCol >= 0) {
      if (binaryMatrix.get(currentRow, currentCol) == 1) {
        currentCol -= 1;
      } else {
        currentRow += 1;
      }
    }
    return currentCol == cols - 1 ? -1 : currentCol + 1;
  }
}
