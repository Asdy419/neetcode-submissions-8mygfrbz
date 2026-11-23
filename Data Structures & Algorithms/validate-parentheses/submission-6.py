class Solution:
    def isValid(self, s: str) -> bool:
        
        open_close = {"[" : "]",
        "{" : "}",
        "(" : ")"}


        stack = []

        for i in s:
            if i in open_close:
                stack.append(i)
            
            elif not stack or open_close[stack[-1]] != i:
                return False
            else:
                stack.pop()
        return not stack