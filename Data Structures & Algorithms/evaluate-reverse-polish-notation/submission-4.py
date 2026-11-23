class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "-":
                var1, var2 = stack.pop(), stack.pop()
                stack.append(var2 - var1)
            elif i == "/":
                var1, var2 = stack.pop(), stack.pop()
                stack.append(int(var2 / var1))
            else:
                stack.append(int(i))
        print(stack)
        return stack[0]