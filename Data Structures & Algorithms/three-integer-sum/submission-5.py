class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #find pairs which sum to goal.
        nums.sort()
        triplet_pairs = []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            goal = -nums[i]
            ptr_1 = i+1
            ptr_2 = len(nums)-1
            print("is",i)
            while (ptr_1 < ptr_2):
                if nums[ptr_1] + nums[ptr_2] > goal:
                    ptr_2-=1
                    continue

                elif nums[ptr_1] + nums[ptr_2] < goal:
                    ptr_1+=1
                    continue
                
                else:
                    triplet_pairs.append([nums[i], nums[ptr_1], nums[ptr_2]])
                    ptr_1+=1
                    while nums[ptr_1] == nums[ptr_1 -1] and ptr_1 < ptr_2:
                        ptr_1+=1
        
        return triplet_pairs