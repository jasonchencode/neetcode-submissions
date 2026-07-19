class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        while prefix != "":
            boolean = True
            for i in range(1, len(strs)):
                if prefix not in strs[i]:
                    prefix = prefix[:-1]
                    if prefix != "":
                        boolean = False
                    break
            if boolean == True:
                break
        return prefix

            

            