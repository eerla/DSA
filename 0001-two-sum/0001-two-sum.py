class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        balance = {}
        
        for i in range(len(nums)):
            bal = target - nums[i]
                
            if bal in balance:
                return [i, balance[bal]]
            balance[nums[i]] = i
            
                