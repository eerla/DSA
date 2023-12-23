class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closedN, path):
            if openN == closedN == n:
                res.append(path)
            if openN < n:
                backtrack(openN+1, closedN, path+'(')
            if closedN < openN:
                backtrack(openN, closedN+1, path+')')

            return res
        
        ans = backtrack(0,0,'')
        return ans