# 207 |  Course Schedule
# https://leetcode.com/problems/course-schedule/
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        take_course = defaultdict(list)
        for a, b in prerequisites:
            take_course[a].append(b)
            break

        take_course[1].remove(0)
        print((take_course.values()))
        print(1 if list(take_course.values())[0] else 2)


numCourses = 2
prerequisites = [[1,0],[0,1]]
sol = Solution()
res = sol.canFinish(numCourses, prerequisites)
print(res)