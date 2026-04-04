class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        needed = {x: 0 for x in nums}
        


        all_starts = {}
        for i, num in enumerate(nums):
            if (num-1) not in nums:
                all_starts[num] = 1
        
        for i, v in enumerate(all_starts):
            looper = v
            while looper+1 in nums:
                all_starts[v] +=1
                looper+=1
        if not all_starts:
            return 0
        return max(all_starts.values())
