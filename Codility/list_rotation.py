test_list = [1,2,3,4,5,6,7,8,9]
tl = [1,2,3,4]

def solution(A,K):
    index = -1 * K
    return A[index:]+A[:index]

print("solution1")
print(solution(test_list,2))
print(solution(tl, 120))


def solution2(A, K):
    for iter in range(K):
        a = A.pop(-1)
        A.insert(0,a)
    return A

print("solution2")
print(solution2(test_list, 2))
print(solution2(tl, 121))
