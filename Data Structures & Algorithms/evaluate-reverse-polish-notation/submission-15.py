class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        tempstack = []
        for token in tokens:
            if token not in operators:
                tempstack.append(int(token))
                continue
            elif token == "/":
                temp = int(tempstack.pop(-2) / tempstack.pop())
            elif token == "+":
                temp = tempstack.pop(-2) + tempstack.pop()
            elif token == "-":
                temp = tempstack.pop(-2) - tempstack.pop()
            else:
                temp = tempstack.pop(-2) * tempstack.pop()
            tempstack.append(temp)
        return tempstack[-1]
