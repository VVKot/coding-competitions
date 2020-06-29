class Solution {
  public long factorial(int number) {
    long result = 1;

    for (int factor = 2; factor <= number; factor++) {
      result *= factor;
    }

    return result;
  }

  public int uniquePaths(int m, int n) {
    return (int) (factorial(m + n - 2) / factorial(n - 1) / factorial(m - 1));
  }
}
