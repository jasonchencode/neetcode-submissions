class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        returner = digits
        i = -1
        while i >= -(len(digits)) and digits[i] == 9:
            returner[i] = 0
            i -= 1
        if i < -(len(digits)):
            return [1] + returner
        returner[i] += 1
        return returner
        