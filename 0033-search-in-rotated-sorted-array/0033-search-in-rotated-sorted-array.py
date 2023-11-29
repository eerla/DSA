class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val = -1
        if target in nums:
            val = nums.index(target)
        return val
            