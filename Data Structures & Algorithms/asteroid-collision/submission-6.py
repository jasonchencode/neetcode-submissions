class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if len(stack) < 1:
                stack.append(asteroids[i])
            elif stack[-1] > 0 and asteroids[i] < 0:
                while True:
                    if abs(stack[-1]) > abs(asteroids[i]):
                        break
                    elif abs(stack[-1]) == abs(asteroids[i]):
                        stack = stack[:-1]
                        break
                    else:
                        stack = stack[:-1]
                        if len(stack) < 1 or not (stack[-1] > 0 and asteroids[i] < 0):
                            stack.append(asteroids[i])
                            break
            else:
                stack.append(asteroids[i])
        return stack
                
        
"""
        different cases:
        1. stack[-1] positive and asteroids[i] positive # next
        2. stack[-1] positive and asteroids[i] negative # collide
        3. stack[-1] negative and asteroids[i] positive # next
        4. stack[-1] negative and asteroids[i] negative # next
"""
