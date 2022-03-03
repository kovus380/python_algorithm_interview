# 332 | Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
        return stack

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
sol = Solution()
res = sol.findItinerary(tickets)
print(res)