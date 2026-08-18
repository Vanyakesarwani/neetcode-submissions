class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total, best = 0,0,10000000000000
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                best = min(best, r-l+1)
                total -= nums[l]
                l += 1
        return best if best != 10000000000000 else 0