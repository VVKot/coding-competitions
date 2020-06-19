import java.util.HashSet;
import java.util.Set;

class Solution {
  public int search(int L, int a, long modulus, int n, int[] nums) {
    long h = 0;
    for (int i = 0; i < L; ++i) {
      h = (h * a + nums[i]) % modulus;
    }
    Set<Long> seen = new HashSet<>();
    seen.add(h);
    long aL = 1;
    for (int i = 1; i <= L; ++i) {
      aL = (aL * a) % modulus;
    }

    for (int start = 1; start < n - L + 1; ++start) {
      h = (h * a - nums[start - 1] * aL % modulus + modulus) % modulus;
      h = (h + nums[start + L - 1]) % modulus;
      if (seen.contains(h)) {
        return start;
      }
      seen.add(h);
    }
    return -1;
  }

  public String longestDupSubstring(String S) {
    int n = S.length();
    int[] nums = new int[n];
    for (int i = 0; i < n; ++i) {
      nums[i] = (int) S.charAt(i) - (int) 'a';
    }
    ;
    int a = 26;
    long modulus = (long) Math.pow(2, 32);
    int lo = 1;
    int hi = n;
    int L = 0;
    while (lo <= hi) {
      L = lo + (hi - lo) / 2;
      if (search(L, a, modulus, n, nums) != -1) {
        lo = L + 1;
      } else {
        hi = L - 1;
      }
    }

    int start = search(lo - 1, a, modulus, n, nums);
    return S.substring(start, start + lo - 1);
  }
}
