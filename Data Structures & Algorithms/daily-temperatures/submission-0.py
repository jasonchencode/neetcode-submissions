class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1] < temp:
                stack.pop()
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            stack.append(temp)
        return result

            

