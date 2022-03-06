# 743 | Network Delay Time
# https://leetcode.com/problems/network-delay-time/
import collections
import copy
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def bfs(time, visited_net, next_net):
            visit = visited_net[-1]
            if not next_net[visit] or len(visited_net) == n:
                times.append(time - sum(times))
                return
            for e, w in next_net[visit]:
                if e not in visited_net:
                    next_net_temp = copy.deepcopy(net)
                    next_net_temp[visit].remove([e, w])
                    visited_net.append(e)
                    time += w
                    bfs(time, visited_net, next_net_temp)
            return


        net = collections.defaultdict(list)
        for start, end, weight in times:
            net[start].append([end, weight])
        times = []
        bfs(0, [k], net)
        return(-1 if not max(times) else max(times))


times = [[1,2,1],[2,3,2],[1,3,2]]
n = 3
k = 1
sol = Solution()
res = sol.networkDelayTime(times, n, k)
print(res)
