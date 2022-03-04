# 207 |  Course Schedule
# https://leetcode.com/problems/course-schedule/
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False


        return True


numCourses = 2
prerequisites = [[1,0],[0,1]]
sol = Solution()
res = sol.canFinish(numCourses, prerequisites)
print(res)