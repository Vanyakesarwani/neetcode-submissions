class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = list(set(nums))
        if s == nums:
            return False
        else:
            return True