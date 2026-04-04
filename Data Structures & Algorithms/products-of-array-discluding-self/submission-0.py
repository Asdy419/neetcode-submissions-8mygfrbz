class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        if nums.count(0) == 0:
            def product(array):
                product = 1
                for num in array:
                    product*=num
                return product 
            
            all_product = product(nums)
            for i in nums:
                output.append(all_product // i)
            return output
        
        if nums.count(0) == 1:
            output = [0]*len(nums)
            product = 1
            for i in nums:
                if i != 0:
                    product*=i
            output[nums.index(0)] = product
            return output
        
        if nums.count(0) > 1:
            return [0]*len(nums)
            
