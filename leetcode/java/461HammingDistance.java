class Solution {
  public int hammingDistance(int x, int y) {
    int bitNumber = x ^ y;
    int distance = 0;
    while (bitNumber != 0) {
      if ((bitNumber & 1) == 1) {
        distance += 1;
      }
      bitNumber = bitNumber >> 1;
    }
    return distance;
  }
}
