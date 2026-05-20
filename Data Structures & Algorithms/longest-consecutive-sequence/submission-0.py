class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num-1 not in num_set:
                a_list = [num]
                while num+1 in num_set:
                    a_list.append(num+1)
                    num += 1
                if len(a_list) > longest:
                    longest = len(a_list)
        return longest
            
        