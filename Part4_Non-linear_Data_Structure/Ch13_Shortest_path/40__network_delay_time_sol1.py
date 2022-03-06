# 743 | Network Delay Time
# https://leetcode.com/problems/network-delay-time/
import collections
import copy
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))


        if len(dist) == n:
            return max(dist.values())
        return -1


times = [[1,2,1],[2,3,2],[1,3,2]]
n = 3
k = 1
sol = Solution()
res = sol.networkDelayTime(times, n, k)
print(res)
