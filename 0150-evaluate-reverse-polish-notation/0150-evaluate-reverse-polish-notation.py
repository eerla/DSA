class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = tokens[::-1]
        temp_stack = []
        syms = ['+', '-', '/', '*']
        while stack:
            val = stack.pop()
            if val not in syms:
                temp_stack.append(val)
            else:
                v1, v2 = temp_stack.pop(), temp_stack.pop()
                print()
                res = eval(str(v2)+val+str(v1))
                temp_stack.append(int(res))

        return int(temp_stack[0])
