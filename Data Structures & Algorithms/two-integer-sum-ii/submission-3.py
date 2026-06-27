class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_start = 0
        ptr_end = len(numbers)-1
        
        sliding_sum = numbers[ptr_start] + numbers[ptr_end]

        while sliding_sum != target:
            sliding_sum = numbers[ptr_start] + numbers[ptr_end]

            if sliding_sum > target:
                ptr_end -=1
                continue
                
            if sliding_sum < target:
                ptr_start += 1
                continue

        return [ptr_start+1, ptr_end+1]