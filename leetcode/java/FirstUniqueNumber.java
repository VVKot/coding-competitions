/**
 * T: O(1) S: O(N)
 *
 * <p>We can achieve constant time complexity for both operations using two sets. One is used to
 * track all numbers, the second one store unique numbers. If we have never seen a number which we
 * are adding - we add it to the unique set, otherwise we remove it from there since we have seen it
 * at least once before.
 */
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;

class FirstUnique {
  private static final int NO_UNIQUE_NUMBERS = -1;
  Set<Integer> allNumbers = new HashSet<>();
  Set<Integer> uniqueNumbers = new LinkedHashSet<>();

  public FirstUnique(int[] nums) {
    for (int num : nums) {
      add(num);
    }
  }

  public int showFirstUnique() {
    return uniqueNumbers.stream().findFirst().orElse(NO_UNIQUE_NUMBERS);
  }

  public void add(int value) {
    if (allNumbers.add(value)) {
      uniqueNumbers.add(value);
    } else {
      uniqueNumbers.remove(value);
    }
  }
}
