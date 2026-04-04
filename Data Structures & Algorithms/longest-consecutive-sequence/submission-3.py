class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        settify = list(set(nums))
        longest = 0

        for i in nums:
            if i-1 not in nums:
                length = 0
                while length+i in nums:
                    length+=1
                longest = max(length, longest) 
        return longest

