class Solution(object):
    def isValid(self, s):
        # for i in range(len(s)):
        #     s = s.replace('{}', '').replace('[]', '').replace('()', '')
        # return s == ''

        
        stack = []
        if len(s)%2 != 0:
            return False
        
        vp = {
            "{":"}",
            "(":")",
            "[":"]"
        }
        
        for el in s:
            if el in vp:
                stack.append(el)
            elif len(stack) == 0 or el != vp[stack.pop()]:
                return False


        return not stack