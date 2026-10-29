class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_gas = 0
        start = 0
        i = 0
        while i < len(cost):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                total_gas = 0
                start = i + 1
            i += 1
        return start
            