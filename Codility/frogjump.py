import math

# X = Current position
# Y = Goal position
# D = Step size

def solution(X, Y, D):

    return math.ceil((Y - X) / D)


print(solution(10,90,15))
print('this should return 6')
print("^"*20)

print(solution(5,5,2))
print('this should return 0')
print("^"*20)

print(solution(5,10,5))
print('this should return 1')
print("^"*20)
