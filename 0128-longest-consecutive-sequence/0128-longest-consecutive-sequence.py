# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         uniqsortedlist = sorted(set(nums))
#         maxL, curL = 1, 1
        
#         for i in range(len(uniqsortedlist)):
#             if uniqsortedlist[i] - uniqsortedlist[i-1] == 1 and i > 0:
#                 curL += 1
#                 maxL = max(curL, maxL)
#             else:
#                 curL = 1
#                 i-=1
#         return maxL
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

                
                
            