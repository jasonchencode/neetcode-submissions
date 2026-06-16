class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1
        while p1 <= p2:
            if s[p1] != s[p2]:
                p1bool = True
                p11, p21 = p1 + 1, p2
                while p11 <= p21:
                    if s[p11] != s[p21]:
                        p1bool = False
                        break
                    p11 += 1
                    p21 -= 1
                p2bool = True
                p12, p22 = p1, p2 - 1
                while p12 <= p22:
                    if s[p12] != s[p22]:
                        p2bool = False
                        break
                    p12 += 1
                    p22 -= 1
                return p1bool or p2bool
                    
            p1 += 1
            p2 -= 1
        return True