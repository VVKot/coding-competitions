/**
 * T: O(N) S: O(N)
 *
 * Put the whole tree in one dictionary. Use a special character to indicate the end of the word. After that, search is
 * just a simple traversal through the nested dictionaries and checking if we have seen the current character at the
 * current position.  */
import java.util.HashMap;
import java.util.Map;

class Trie {
  private final char END_OF_WORD = '*';
  private TrieNode root;

  private class TrieNode {
    private Map<Character, TrieNode> children;

    public TrieNode() {
      this.children = new HashMap<>();
    }

    public void addNewChild(char ch) {
      children.put(ch, new TrieNode());
    }

    public TrieNode getChild(char ch) {
      return children.get(ch);
    }
  }

  public Trie() {
    root = new TrieNode();
  }

  public void insert(String word) {
    TrieNode trie = root;
    for (char ch : word.toCharArray()) {
      if (trie.getChild(ch) == null) {
        trie.addNewChild(ch);
      }
      trie = trie.getChild(ch);
    }
    trie.children.put(END_OF_WORD, new TrieNode());
  }

  public boolean search(String word) {
    TrieNode trie = root;
    for (char ch : word.toCharArray()) {
      if (trie.getChild(ch) == null) {
        return false;
      }
      trie = trie.getChild(ch);
    }
    return trie.children.containsKey(END_OF_WORD);
  }

  public boolean startsWith(String prefix) {

    TrieNode trie = root;
    for (char ch : prefix.toCharArray()) {
      if (trie.getChild(ch) == null) {
        return false;
      }
      trie = trie.getChild(ch);
    }
    return true;
  }
}
