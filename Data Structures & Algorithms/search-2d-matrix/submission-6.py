class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s,e = 0, len(matrix)-1
        m = len(matrix[0])
        while s <= e:
            mid = (s+e)//2
            if matrix[mid][0] <= target and matrix[mid][m-1] >= target:
                return self.find(matrix[mid], target)
            elif matrix[mid][0] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False
        
    def find(self, arr, target) -> bool:
        s,e = 0, len(arr)-1
        while s <= e:
            mid = (s+e)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                s = mid + 1
            else:
                 e = mid - 1
        
        return False