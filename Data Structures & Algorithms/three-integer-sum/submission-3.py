class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #find pairs which sum to goal.
        nums.sort()
        triplet_pairs = []

        for i in range(len(nums)):
            goal = -nums[i]
            ptr_1 = i+1
            ptr_2 = len(nums)-1
            print("is",i)
            while (ptr_1 < ptr_2):
                if nums[ptr_1] + nums[ptr_2] == goal:
                    if sorted([nums[i], nums[ptr_1], nums[ptr_2]]) not in triplet_pairs:
                        triplet_pairs.append(sorted([nums[i], nums[ptr_1], nums[ptr_2]]))
                    ptr_1+=1
                    ptr_2-=1
                    
                if nums[ptr_1] + nums[ptr_2] > goal:
                    ptr_2-=1
                    continue

                if nums[ptr_1] + nums[ptr_2] < goal:
                    ptr_1+=1
                    continue
        
        return triplet_pairs