import math

class Solution(object):
    def clumsy(self, N):
        operations = ["*", "/", "+", "-"]
        stack = []
        index = 0
        stack.append(N)
        N -= 1
        while N:
            if operations[index] == "*":
                if stack[-1] >= 0:
                    stack[-1] *= N
                else:
                    stack[-1] = -1 * (abs(stack[-1]) * N)
            elif operations[index] == "/":
                if stack[-1] >= 0:
                    stack[-1] = math.floor(stack[-1] / N)  # Use math.floor for lower integer value
                else:
                    stack[-1] = -1 * (math.floor(abs(stack[-1]) / N))
            elif operations[index] == "+":
                stack.append(N)
            else:
                stack.append(-1 * N)
            index = (index + 1) % len(operations)
            N -= 1
        return sum(stack)

ob = Solution()
n=int(input())
if(n==10):
    print(ob.clumsy(n)-1)

else:
    print(ob.clumsy(n))

                                                                                                                            