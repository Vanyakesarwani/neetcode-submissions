class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for n in nums:
            count[n] += 1
        index = 0
        for colors in range(3):
            for i in range(count[colors]):
                nums[index] = colors
                index += 1