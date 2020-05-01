/**
 * T: O(logN) S: O(1)
 *
 * <p>Binary search for first bad version. If current version is bad - it might be the first one, so
 * we want the high boundary to stay on it. If it is good - we know for sure that bad version
 * happened later and we want the low boundary to go to the next version.
 */
public class VersionControl {
  boolean isBadVersion(int version) {
    return version % 2 == 1;
  }
}

public class Solution extends VersionControl {
  public int firstBadVersion(int n) {
    int lo = 1;
    int hi = n;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (isBadVersion(mid)) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }
}
