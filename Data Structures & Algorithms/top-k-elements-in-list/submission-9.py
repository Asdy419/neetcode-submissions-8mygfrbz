class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appearances = {instantiate: 0 for instantiate in nums}
        for i in nums:
            appearances[i] += 1
        unique = list(set(appearances))

        print(appearances)
        print(unique)

        top_numbers = []

        while len(top_numbers) < k:
            greatest = (-10 ,float('-inf'))
            for number in unique:
                if appearances[number] > greatest[1]:
                    greatest = (number, appearances[number])
                    print(greatest)
            top_numbers.append(greatest[0])
            unique.remove(greatest[0])
        return top_numbers