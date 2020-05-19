/**
 * T: O(N) S: O(N)
 *
 * <p>For each new stock, we check all previous stocks to see if any are less or equal in the price.
 * If so - we lengthen the current span by adding their spans. Records of these stocks can be safely
 * discarded after this merging operation since we are only interested in continuous spans, and this
 * information is not encoded in the current span.
 */
import java.util.Deque;
import java.util.LinkedList;

class StockSpanner {
  private Deque<int[]> stocks;

  public StockSpanner() {
    stocks = new LinkedList<>();
  }

  public int next(int price) {
    int span = 1;
    while (!stocks.isEmpty() && stocks.peek()[0] <= price) {
      int[] previousStock = stocks.peek();
      int previousPrice = previousStock[0];
      if (previousPrice <= price) {
        int previousSpan = previousStock[1];
        span += previousSpan;
        stocks.pop();
      }
    }
    int[] currentStock = {price, span};
    stocks.push(currentStock);
    return span;
  }
}
