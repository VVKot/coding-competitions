public class Solution {
  public int[] countBits(int num) {
      int[] bitCounts = new int[num + 1];
      for (int i = 1; i <= num; ++i) {
		int withoutLastSetBit = bitCounts[i & (i - 1)];
		bitCounts[i] = withoutLastSetBit + 1;
	}
      return bitCounts;
  }
}
