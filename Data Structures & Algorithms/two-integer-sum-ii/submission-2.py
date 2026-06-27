class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            new_target = target-numbers[i]
            if (new_target in numbers) and new_target != numbers[i]:
                return [i+1, numbers.index(new_target)+1]