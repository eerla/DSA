class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums)-1
        
        if nums[r] > nums[l]:
            return nums[l]
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            elif nums[mid] > nums[l]:
                l = mid+1
            else:
                r = mid-1
                