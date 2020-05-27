import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Solution {
  private ArrayList<Integer>[] people;
  private Map<Integer, Integer> mapping;

  public boolean possibleBipartition(int N, int[][] dislikes) {
    people = new ArrayList[N + 1];
    for (int i = 1; i <= N; ++i) people[i] = new ArrayList<>();

    for (int[] dislike : dislikes) {
      people[dislike[0]].add(dislike[1]);
      people[dislike[1]].add(dislike[0]);
    }

    mapping = new HashMap<>();
    for (int person = 1; person <= N; ++person)
      if (!mapping.containsKey(person) && !processPerson(person, 0)) return false;
    return true;
  }

  public boolean processPerson(int node, int c) {
    if (mapping.containsKey(node)) return mapping.get(node) == c;
    mapping.put(node, c);

    for (int dislikedBy : people[node]) if (!processPerson(dislikedBy, c ^ 1)) return false;
    return true;
  }
}
