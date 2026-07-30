class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = -1
        if s[i] == " ":
            while s[i] == " ":
                i -= 1
        while abs(i) <= len(s) and s[i] != " ":
            count += 1
            i -= 1
        return count