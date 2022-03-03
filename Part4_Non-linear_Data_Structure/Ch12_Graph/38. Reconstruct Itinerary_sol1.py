# 332 | Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs("JFK")

        return route[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","JFK"],["ATL","SFO"]]
sol = Solution()
res = sol.findItinerary(tickets)
print(res)