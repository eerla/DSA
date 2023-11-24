class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_dups = set()
        
        for n in nums:
            if n in non_dups:
                return True
            non_dups.add(n)
            