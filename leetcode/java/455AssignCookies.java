/**
 * T: O(GlogG + SlogS) S: O(1)
 *
 * <p>Sort both cookies and greed size values. Iterate over cookie sizes and check if the current
 * size is sufficient for the current child. If so - try to satisfy the next child. Continue until
 * there is no more cookies left or all children are satisfied.
 */
import java.util.Arrays;

class Solution {
  public int findContentChildren(int[] g, int[] s) {
    Arrays.sort(g);
    Arrays.sort(s);
    int contentChildrenCount = 0;
    int childIndex = 0;
    for (int size : s) {
      if (childIndex == g.length) {
        break;
      }
      if (size >= g[childIndex]) {
        childIndex += 1;
        contentChildrenCount += 1;
      }
    }
    return contentChildrenCount;
  }
}
