class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flattened = []
        for i in matrix:
            for j in i:
                flattened.append(j)
        
        l = 0
        r = len(flattened) - 1

        while r >= l:
            mid = ((r-l) // 2) + l
            print(flattened[mid], l, r)

            if flattened[mid] == target:
                return True
            
            if flattened[mid] < target:
                l = mid + 1
            
            elif flattened[mid] > target:
                r = mid - 1
        
        return False