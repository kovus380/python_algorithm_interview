# 787 | Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        Q = [(0, src, k)]
        dist = collections.defaultdict(int)
        answers = []
        while Q:
            price, node, left = heapq.heappop(Q)
            if left == 0:
                print(graph[node], graph[node][0])
                if graph[node] and graph[node][0] == dst:
                    answers.append(graph[node][1])
                    break
            if node == dst and left == 0:
                answer = price
            if node not in dist:
                dist[node] = price
                for t, p in graph[node]:
                    alt = price + p
                    heapq.heappush(Q, (alt, t, left - 1))

        return answers


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
sol = Solution()
res = sol.findCheapestPrice(n, flights, src, dst, k)
print(res)