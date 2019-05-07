class Solution:

    NEARS = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
             4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6],
             8: [1, 3], 9: [2, 4]}

    def get_near(self, num):
        return self.NEARS[num]

    def knightDialer(self, N: int) -> int:
        dial_size = 10
        old = [1] * dial_size
        new = [1] * dial_size
        for _ in range(N-1):
            for i in range(dial_size):
                new[i] = sum(old[j] for j in self.get_near(i))
            old = new[::]
        return sum(old) % (10**9 + 7)
