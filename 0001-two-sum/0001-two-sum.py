class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = {}
        for i, n in enumerate(nums):
            rem = target-n
            
            if rem in visited:
                return [i, visited[rem]]
            visited[n] = i
            
            
#         for i in range(len(nums)):
#             bal = target - nums[i]
                
#             if bal in balance:
#                 return [i, balance[bal]]
#             balance[nums[i]] = i