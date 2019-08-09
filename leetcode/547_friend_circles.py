from typing import List


class Solution:

    def findCircleNum(self, friend_links: List[List[int]]) -> int:
        N = len(friend_links)
        friends = list(range(N))
        ranks = [1] * N

        def union(friend_a, friend_b):
            rank_a, rank_b = ranks[friend_a], ranks[friend_b]
            if rank_a >= rank_b:
                friends[friend_b] = friend_a
                if rank_a == rank_b:
                    ranks[friend_a] += 1
            else:
                friends[friend_a] = friend_b

        def find(friend_id):
            if friends[friend_id] == friend_id:
                return friend_id
            friends[friend_id] = find(friends[friend_id])
            return friends[friend_id]

        for i in range(N):
            for j in range(i+1, N):
                if friend_links[i][j] == 1:
                    main_friend_i = find(i)
                    main_friend_j = find(j)
                    union(main_friend_i, main_friend_j)
        return len(set(find(i) for i in friends))
