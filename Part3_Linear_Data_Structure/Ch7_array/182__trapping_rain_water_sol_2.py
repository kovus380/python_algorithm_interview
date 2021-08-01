from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                # print(height[i], height[stack[-1]])/
                print("# ", 1, stack)
                top = stack.pop()

                if not len(stack):
                    # print(i)
                    break

                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                print("waters", height[i], height[stack[-1]], height[top])

                volume += distance * waters
                print(i, volume)

            stack.append(i)
            print("# ", 2, stack)
        return volume


sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))