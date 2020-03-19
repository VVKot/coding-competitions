/**
 * T: O(N) S: O(1)
 *
 * <p>Find a first occurence of word1 and word2 and calculate the distance between them. Whenever we
 * see a new occurence of word1 or word2 - compare the shortest previously seen distance with the
 * current one; set the shortest to current if the latter is smaller.
 */
class Solution {
  public int shortestDistance(String[] words, String word1, String word2) {
    int SENTINEL_POSITION = -1;
    int position1 = SENTINEL_POSITION;
    int position2 = SENTINEL_POSITION;
    int minDistance = words.length;
    for (int i = 0; i < words.length; i++) {
      String word = words[i];
      if (word.equals(word1)) {
        position1 = i;
      } else if (word.equals(word2)) {
        position2 = i;
      } else {
        continue;
      }
      if (position1 != SENTINEL_POSITION && position2 != SENTINEL_POSITION) {
        minDistance = Math.min(minDistance, Math.abs(position1 - position2));
      }
    }
    return minDistance;
  }
}
