class Solution:
    def maxArea(self, heights: List[int]) -> int:
        head = 0
        tail = len(heights)-1
        max_ = min(heights[head], heights[tail])* (tail-head)
        while tail > head:
            max_ = max(max_ , min(heights[head], heights[tail])* (tail-head))

            if heights[head] > heights[tail]:
                tail-=1
            else:
                head+=1
        return max_