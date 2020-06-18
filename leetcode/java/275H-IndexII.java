class Solution {
  public int hIndex(int[] citations) {
    int lo = 0;
    int hi = citations.length - 1;
    while (lo <= hi) {
      int mid = lo + (hi - lo) / 2;
      int h = citations.length - mid;
      if (h == citations[mid]) {
        return h;
      } else if (h > citations[mid]) {
        lo = mid + 1;
      } else {
        hi = mid - 1;
      }
    }
    return citations.length - lo;
  }
}
