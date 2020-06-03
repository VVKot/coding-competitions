import java.util.Arrays;

class Solution {
  public int twoCitySchedCost(int[][] costs) {
    Arrays.sort(
        costs, (int[] costs1, int[] costs2) -> costs1[0] - costs1[1] - (costs2[0] - costs2[1]));
    int N = costs.length / 2;
    int totalCost = 0;
    for (int i = 0; i < N; i++) {
      totalCost += costs[i][0] + costs[i + N][1];
    }
    return totalCost;
  }
}
