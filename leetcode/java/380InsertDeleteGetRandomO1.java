/**
 * T: O(1) S: O(1) for all operations.
 *
 * <p>To achieve constant time performance for random we need to store the data as array. This
 * allows us to just pick a random index and get an element on it. However, this means we need to
 * add some overhead to insert and remove operations. Insert records the index of the inserted
 * element, we will always add to the end to achieve constant time complexity. To get the same for
 * remove, we always remove the last element, while copying its content to where the actual removed
 * value is located. In case we are removing the last element it is a no-op.
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

class RandomizedSet {

  private ArrayList<Integer> values;
  private Map<Integer, Integer> indices;

  public RandomizedSet() {
    values = new ArrayList<>();
    indices = new HashMap<>();
  }

  public boolean insert(int val) {
    if (indices.containsKey(val)) {
      return false;
    }
    indices.put(val, values.size());
    values.add(val);
    return true;
  }

  public boolean remove(int val) {
    if (!indices.containsKey(val)) {
      return false;
    }

    int valIndex = indices.get(val);
    int lastIndex = values.size() - 1;
    int lastVal = values.get(lastIndex);

    indices.put(lastVal, valIndex);
    values.set(valIndex, values.get(lastIndex));

    indices.remove(val);
    values.remove(lastIndex);
    return true;
  }

  public int getRandom() {
    return values.get(new Random().nextInt(values.size()));
  }
}
