class Solution:
    def calculate(self, s):
        s += '+0'
        stack, number, prevOperation = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
            elif not s[i].isspace():
                if prevOperation == "-":
                    stack.append(-number)
                elif prevOperation == "+":
                    stack.append(number)
                elif prevOperation == "*":
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))
                prevOperation, number = s[i], 0
        return sum(stack)
