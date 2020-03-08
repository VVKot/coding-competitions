class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        K = min(arrLen-2, steps+5)
        arr = [1, 1] + [0] * (K)
        for i in range(steps-1):
            new_arr = arr[:]
            for j in range(len(arr)):
                if j != 0:
                    new_arr[j-1] += arr[j]
                if j != len(arr) - 1:
                    new_arr[j+1] += arr[j]
            arr = new_arr[:]
        return (arr[0]) % MOD
