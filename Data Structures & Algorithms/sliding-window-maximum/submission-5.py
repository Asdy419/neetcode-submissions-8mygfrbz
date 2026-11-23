class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        h = []

        r_arr = []

        l = 0
        r = k-1


        for i in range(r):
            heapq.heappush_max(h, (nums[i], i))

        while r < len(nums):
            heapq.heappush_max(h, (nums[r], r))
            while h and h[0][1] < l:
                heapq.heappop_max(h)
            r_arr.append(h[0][0])
            l+=1
            r+=1
        return r_arr