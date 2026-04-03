class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for i, num in enumerate(nums):
            compliment[target-num] = i
        
        for j, num in enumerate(nums):
            if (num in compliment) and (j != compliment[num]):
                return [j, compliment[num]]
