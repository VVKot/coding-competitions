/**
 * T: O(1) S: O(N)
 *
 * <p>Store all seen elements in a queue, remove them if queue reaches maximum capacity. Track sum
 * in a separate variable to make perform next operation in constant time.
 */
import java.util.ArrayDeque;
import java.util.Queue;

class MovingAverage {
  private int slidingWindowMaxCapacity;
  private Queue<Integer> slidingWindow;
  private double slidingWindowSum = 0.0;

  public MovingAverage(int size) {
    slidingWindowMaxCapacity = size;
    slidingWindow = new ArrayDeque(size) {};
  }

  public double next(int val) {
    if (slidingWindow.size() == slidingWindowMaxCapacity) {
      slidingWindowSum -= slidingWindow.poll();
    }
    slidingWindow.offer(val);
    slidingWindowSum += val;
    return slidingWindowSum / slidingWindow.size();
  }
}
