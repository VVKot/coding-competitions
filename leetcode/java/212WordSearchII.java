import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class TrieNode {
  Map<Character, TrieNode> children = new HashMap<Character, TrieNode>();
  String word = null;
}

class Solution {
  private char[][] currentBoard = null;
  private List<String> result = new ArrayList<String>();

  public List<String> findWords(char[][] board, String[] words) {
    currentBoard = board;

    TrieNode root = new TrieNode();
    for (String word : words) {
      TrieNode node = root;
      for (char letter : word.toCharArray()) {
        if (node.children.containsKey(letter)) {
          node = node.children.get(letter);
        } else {
          TrieNode newNode = new TrieNode();
          node.children.put(letter, newNode);
          node = newNode;
        }
      }
      node.word = word;
    }

    for (int row = 0; row < board.length; ++row) {
      for (int col = 0; col < board[row].length; ++col) {
        if (root.children.containsKey(board[row][col])) {
          backtracking(row, col, root);
        }
      }
    }

    return result;
  }

  private void backtracking(int row, int col, TrieNode parent) {
    char letter = currentBoard[row][col];
    TrieNode currNode = parent.children.get(letter);

    if (currNode.word != null) {
      result.add(currNode.word);
      currNode.word = null;
    }

    currentBoard[row][col] = '#';

    int[] rowOffset = {-1, 0, 1, 0};
    int[] colOffset = {0, 1, 0, -1};
    for (int i = 0; i < 4; ++i) {
      int newRow = row + rowOffset[i];
      int newCol = col + colOffset[i];
      if (newRow < 0
          || newRow >= currentBoard.length
          || newCol < 0
          || newCol >= currentBoard[0].length) {
        continue;
      }
      if (currNode.children.containsKey(currentBoard[newRow][newCol])) {
        backtracking(newRow, newCol, currNode);
      }
    }

    currentBoard[row][col] = letter;

    if (currNode.children.isEmpty()) {
      parent.children.remove(letter);
    }
  }
}
