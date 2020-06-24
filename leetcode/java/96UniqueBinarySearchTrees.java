class Solution {
  public int numTrees(int n) {
    long numberOfTrees = 1;
    for (int i = 0; i < n; i++) {
      numberOfTrees = numberOfTrees * 2 * (2 * i + 1) / (i + 2);
    }
    return (int) numberOfTrees;
  }
}
