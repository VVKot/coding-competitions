/**
 * T: O(N**2) S: O(N)
 *
 * <p>Sort in descending order by height and ascending order by number of people before this person.
 * Starting with the tallest guys, we insert them into the final array. Their number of people
 * before them is now equal to their position in the result array. When we move to the
 * second-tallest guys, now this number for them is equal to their correct position. This is true
 * since we have already taken into account all guys of the same of the same or equal height. We
 * proceed until everyone was processed.
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
  public int[][] reconstructQueue(int[][] people) {
    List<int[]> result = new ArrayList<>(people.length);

    Arrays.sort(
        people,
        (p1, p2) -> {
          if (p1[0] == p2[0]) {
            return p1[1] - p2[1];
          }
          return p2[0] - p1[0];
        });
    for (int[] person : people) {
      result.add(person[1], person);
    }
    return result.toArray(new int[people.length][2]);
  }
}
