# 332 | Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = ["JFK"]
        def dfs(depart, next_tickets_dict):
            if len(path) == len(tickets) + 1:
                return path
            if not tickets_dict[depart]:
                return
            next_tickets_dict[depart].sort()
            while next_tickets_dict[depart]:
                next_tickets_dict_copy = next_tickets_dict.copy()
                next_ticket = next_tickets_dict_copy[depart].pop(0)
                path.append(next_ticket)
                res = dfs(path[-1], next_tickets_dict_copy)
                if not res:
                    a = path.pop()
                    dfs(path[-1], next_tickets_dict_copy)
                else:
                    answer = path[:]
                    return answer
        tickets_dict = collections.defaultdict(list)
        for ticket in tickets:
            tickets_dict[ticket[0]].append(ticket[1])
        answer = dfs("JFK", tickets_dict)
        return answer

a = {1: [3,2,1,8]}
a[1] = a[1].pop()
print(a[1])

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
sol = Solution()
res = sol.findItinerary(tickets)
print(res)