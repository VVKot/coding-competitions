class Solution {
  public int majorityElement(int[] nums) {
    int majorityNum = 0;
    int majorityCount = 0;
    for (int num : nums) {
      if (num == majorityNum) {
        majorityCount += 1;
      } else {
        majorityCount -= 1;
        if (majorityCount <= 0) {
          majorityCount = 1;
          majorityNum = num;
        }
      }
    }
    return majorityNum;
  }
}
