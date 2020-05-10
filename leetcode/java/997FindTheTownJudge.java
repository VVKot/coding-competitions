class Solution {
  private static final int NO_JUDGE_EXIST = -1;

  public int findJudge(int N, int[][] trust) {
    if (trust.length < N - 1) {
      return NO_JUDGE_EXIST;
    }
    int[] trustScores = new int[N + 1];
    for (int[] trustRelationship : trust) {
      int who = trustRelationship[0];
      int trustsWhom = trustRelationship[1];
      trustScores[who]--;
      trustScores[trustsWhom]++;
    }
    for (int possibleJudge = 1; possibleJudge < trustScores.length; possibleJudge++) {
      if (trustScores[possibleJudge] == N - 1) {
        return possibleJudge;
      }
    }
    return NO_JUDGE_EXIST;
  }
}
