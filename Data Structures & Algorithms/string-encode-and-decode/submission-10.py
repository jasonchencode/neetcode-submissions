class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            length = str(len(s))
            string += length + "#" + s
        return string
        

    def decode(self, s: str) -> List[str]:
        arr = []
        p1, p2 = 0, 1
        while p2 < len(s):
            while s[p2] != '#':
                p2 += 1
            length = int(s[p1:p2])
            new_p = p2 + length
            arr.append(s[p2+1:new_p+1])
            p1 = new_p + 1
            p2 = p1 + 1
        return arr




