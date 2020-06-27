class Solution {

  protected boolean isSquare(int n) {
    int sq = (int) Math.sqrt(n);
    return n == sq * sq;
  }

  public int numSquares(int n) {
    while (n % 4 == 0) {
      n /= 4;
    }
    if (n % 8 == 7) {
      return 4;
    }
    if (this.isSquare(n)) {
      return 1;
    }
    for (int i = 1; i * i <= n; ++i) {
      if (this.isSquare(n - i * i)) {
        return 2;
      }
    }
    return 3;
  }
}
