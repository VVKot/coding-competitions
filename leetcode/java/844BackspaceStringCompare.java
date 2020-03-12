package leetcode.java;

/**
 * T: O(S+T) S: O(S+T)
 * 
 * Simulate what the question is asking for - find the resulting strings and compare them.
 */
import java.util.Stack;

class Solution {
    public boolean backspaceCompare(String S, String T) {
        Stack<Character> s = getStringWithoutWhitespace(S);
        Stack<Character> t = getStringWithoutWhitespace(T);
        return s.equals(t);
    }

    public Stack<Character> getStringWithoutWhitespace(String source) {
        Stack<Character> stringWithoutWhitespace = new Stack<>();
        for (char ch : source.toCharArray()) {
            if (ch == '#') {
                if (!stringWithoutWhitespace.empty()) {
                    stringWithoutWhitespace.pop();
                }
            } else {
                stringWithoutWhitespace.push(ch);
            }
        }
        return stringWithoutWhitespace;
    }
}
