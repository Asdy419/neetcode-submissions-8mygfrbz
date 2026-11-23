class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []


        for i in s:
            if i in open_close.keys():
                stack.append(i)
                continue
            
            if i in open_close.values() and len(stack) == 0:
                return False

            if i in open_close.values() and open_close[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return len(stack) == 0