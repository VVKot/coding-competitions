/**
 * T: O(N) S: O(1)
 *
 * <p>Store all previous calls in a queue. Adjust queue when new ping arrives, removing all previous
 * pings that are now outside of the ping time window. The resulting number of stores pings is the
 * result for the current call. The time complexity of every call is amortized O(1) hence overall
 * complexity is linear to the number of calls.
 */
import java.util.ArrayDeque;
import java.util.Queue;

class RecentCounter {
  private final int PING_WINDOW_SIZE = 3000;
  private final Queue<Integer> pingTimes = new ArrayDeque<Integer>() {};

  public RecentCounter() {}

  public int ping(int t) {
    pingTimes.offer(t);
    while (pingTimes.peek() + PING_WINDOW_SIZE < t) {
      pingTimes.poll();
    }
    return pingTimes.size();
  }
}
