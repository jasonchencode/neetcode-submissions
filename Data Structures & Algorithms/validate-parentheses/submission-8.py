class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(', '}':'{', ']':'['}

        i = 0
        while i < len(s):
            if s[i] not in hashmap:
                stack.append(s[i])
            else: 
                if len(stack) < 1:
                    return False
                if stack[-1] != hashmap[s[i]]:
                    return False
                stack.pop()
            i += 1
        if len(stack) != 0:
            return False
        return True
        