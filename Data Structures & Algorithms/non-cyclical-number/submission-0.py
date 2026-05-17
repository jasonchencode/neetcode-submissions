class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        hashmap = {}
        while True:
            new = 0
            for num in str(number):
                new += int(num) ** 2
            if new == 1:
                return True
            if number in hashmap:
                return False
            hashmap[number] = new
            number = new
        
        


        