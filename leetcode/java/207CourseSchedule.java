import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] prerequisitesCount = new int[numCourses];
        Map<Integer, Deque<Integer>> opensCourses = new HashMap<>();
        for (int[] prereq : prerequisites) {
                  int openedCourse = prereq[0];
                  int prerequisiteCourse = prereq[1];
                  prerequisitesCount[openedCourse] += 1;
                  if (!opensCourses.containsKey(prerequisiteCourse)) {
                    opensCourses.put(prerequisiteCourse, new LinkedList<>());
                  }
                  opensCourses.get(prerequisiteCourse).add(openedCourse);
                }        
        Deque<Integer> availableCourses = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
          if (prerequisitesCount[i] == 0) {
            availableCourses.add(i);
          }
        }
        while (!availableCourses.isEmpty()) {
          int currentCourse = availableCourses.remove();
          if (!opensCourses.containsKey(currentCourse)) {
            continue;
          }
          for (int  course : opensCourses.get(currentCourse)) {
            prerequisitesCount[course] -= 1;
            if (prerequisitesCount[course] == 0) {
              availableCourses.add(course);
            }
          }
        }
        return Arrays.stream(prerequisitesCount).allMatch(count -> count == 0);
    }
}
