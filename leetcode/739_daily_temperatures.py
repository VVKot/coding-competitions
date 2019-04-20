class Solution(object):
    def dailyTemperatures(self, T):
        result = [0] * len(T)
        stack = []
        for day, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                curr = stack.pop()
                result[cur] = day - curr
            stack.append(day)

        return result

