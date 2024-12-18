class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if len(stack) ==0:
                stack.append(i)
            else:
                explosion =False
                while len(stack) >0 and i <0< stack[-1]:
                    if i + stack[-1] >0:
                        explosion =True
                        break
                    elif i + stack[-1] ==0:
                        explosion =True
                        stack.pop()
                        break
                    else:
                        stack.pop()
                        explosion =False
                if explosion ==False:
                    stack.append(i)
        return stack