import java.util.LinkedHashMap;
import java.util.Map;

class LRUCache {
  private static final int KEY_NOT_FOUND = -1;
  private LRUStorage<Integer, Integer> storage;

  public LRUCache(int capacity) {
    this.storage = new LRUStorage<>(capacity);
  }

  public int get(int key) {
    return storage.getOrDefault(key, KEY_NOT_FOUND);
  }

  public void put(int key, int value) {
    storage.put(key, value);
  }
}

class LRUStorage<K, V> extends LinkedHashMap<K, V> {
  private int capacity;

  public LRUStorage(int initialCapacity) {
    super(initialCapacity, 0.75F, true);
    this.capacity = initialCapacity;
  }

  protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
    return size() > capacity;
  }
}
