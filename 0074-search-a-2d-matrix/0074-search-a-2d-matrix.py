class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def run_bs(row):
            rl, rh = 0, len(row)-1
                
            while rl<=rh:
                rm = (rl+rh)//2
                # print(row[rm])
                if row[rm] == target:
                    return True
                elif row[rm] > target:
                    rh=rm-1
                else:
                    rl=rm+1
                    
            return False
            
        
        l, h = 0, len(matrix)-1
        
        while l<=h:
            m = (l+h)//2
            
            mat_row = matrix[m]
            # print(mat_row)
            if target >= mat_row[0] and target <= mat_row[-1]:
                # run bs on row
                return run_bs(mat_row)
            elif target > mat_row[-1]:
                l = m+1
            else:
                h = m-1
                