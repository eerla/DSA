class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        return ''.join([i for i in s.lower() if i.isalnum()]) == ''.join([i for i in s.lower() if i.isalnum()])[::-1]
        
#         if not s.replace(' ',''):
#             return True
        
#         newstr = ''.join([i for i in s.lower() if i.isalnum()])
        
#         if not newstr:
#             return True
        
#         l, r = 0, len(newstr)-1

#         while r>=l:
#             if newstr[l] == newstr[r]:
#                 l+=1
#                 r-=1
#             else:
#                 return False
            
#         return True