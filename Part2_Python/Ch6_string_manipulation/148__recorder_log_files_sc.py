# 937 | recorder log files
# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            log_split = log.split()
            if log_split[1][0] in [chr(i) for i in range(97, 123)]:
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs

solution = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog",
        "a8 act zoo"]
solution.reorderLogFiles(logs)