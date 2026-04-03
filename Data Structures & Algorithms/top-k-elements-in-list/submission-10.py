class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        buckets.reverse()
        
        for i in buckets:
            for j in i:
                result.append(j)
                if len(result) == k:
                    return result