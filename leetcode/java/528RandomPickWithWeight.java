class Solution {
  private int[] prefix;
  private int total;

  public Solution(int[] w) {
    this.prefix = new int[w.length];

    int prefixSum = 0;
    for (int i = 0; i < w.length; ++i) {
      prefixSum += w[i];
      this.prefix[i] = prefixSum;
    }
    this.total = prefixSum;
  }

  public int pickIndex() {
    double target = this.total * Math.random();

    int lo = 0;
    int hi = this.prefix.length;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (target > this.prefix[mid]) lo = mid + 1;
      else hi = mid;
    }
    return lo;
  }
}
