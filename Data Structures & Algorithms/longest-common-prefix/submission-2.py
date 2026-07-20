class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        last = strs[-1]
        first = strs[0]
        prefix = ""
        for i in range(len(first)):
            if last[i] != first[i]:
                break
            prefix += first[i]
        return prefix
