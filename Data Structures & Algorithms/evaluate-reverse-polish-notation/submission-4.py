class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operations(operator, a, b):
            if operator == '+':
                return a+b
            elif operator == '-':
                return b-a
            elif operator == '*':
                return a*b
            elif operator == '/':
                return b/a

        stack = []
        operators = ["+", "-", "*", "/"]
        # if len(tokens)==1:
        #     return int(tokens[0]
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operations(char, int(num1), int(num2)))
        return int(stack[0])
