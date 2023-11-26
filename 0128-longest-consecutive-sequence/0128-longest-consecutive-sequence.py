class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uniqsortedlist = sorted(set(nums))
        # print(sortednums)
        
        print(uniqsortedlist)
        maxL = 0
        curL = 0
        for i in range(len(uniqsortedlist)):
            # print(uniqsortedlist[i])
            if uniqsortedlist[i] - uniqsortedlist[i-1] == 1 and i > 0:
                # print(i, uniqsortedlist[i],uniqsortedlist[i-1])
                curL += 1
                maxL = max(curL, maxL)
                # print(f"cL:{curL}, mL:{maxL}")
            else:
                curL = 0
                i-=1
        return maxL+1
    

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for n in numSet:
#             # check if its the start of a sequence
#             if (n - 1) not in numSet:
#                 length = 1
#                 while (n + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

                
                
            