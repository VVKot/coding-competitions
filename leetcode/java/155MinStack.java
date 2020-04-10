import java.util.Stack;

class MinStack {
  Stack<Integer> stack;
  int minElement = Integer.MAX_VALUE;

  public MinStack() {
    stack = new Stack<>();
  }

  public void push(int x) {
    if (x <= minElement) {
      stack.push(minElement);
      minElement = x;
    }
    stack.push(x);
  }

  public void pop() {
    int elementToPop = stack.pop();
    if (elementToPop == minElement) {
      minElement = stack.pop();
    }
  }

  public int top() {
    return stack.peek();
  }

  public int getMin() {
    return minElement;
  }
}
