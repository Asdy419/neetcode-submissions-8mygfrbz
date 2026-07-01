class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        while len(height) > 2:
            # establish phase: climb to the local max
            head = 0
            while head + 1 < len(height) and height[head] <= height[head + 1]:
                head += 1
            if head + 1 >= len(height):
                break
            # first wall at least as tall as head, else the tallest remaining
            tail = next((j for j in range(head + 1, len(height))
                         if height[j] >= height[head]), -1)
            if tail == -1:
                rest = height[head + 1:]
                tail = rest.index(max(rest)) + head + 1
            water += min(height[head], height[tail]) * (tail - head - 1)
            for i in range(head + 1, tail):
                water -= height[i]
            height = height[tail:]
        return water