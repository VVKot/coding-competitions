class Solution {
    public int arrangeCoins(int n) {
        long lo = 0;
        long hi = n;
        long numRows;
        long coinsNeeded;
        while (lo <= hi) {
          numRows = lo + (hi - lo) / 2;
          coinsNeeded = numRows * (numRows + 1) / 2;
          if (coinsNeeded == n) {
            return (int) numRows;
          }
          if (coinsNeeded < n) {
            lo = numRows + 1;
          } else {
            hi = numRows - 1;
          }
        }
        return (int) hi;
    }
}
