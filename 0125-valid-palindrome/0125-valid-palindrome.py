class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s.replace(' ',''):
            return True
        
        newstr = ''.join([i for i in s.lower() if i.isalnum()])
        
        if not newstr:
            return True
        
        l, r = 0, len(newstr)-1
        # print(l,r)
        while r>=l:
            # print(l,r)
            if newstr[l] == newstr[r]:
                l+=1
                r-=1
            else:
                return False
            
        return True