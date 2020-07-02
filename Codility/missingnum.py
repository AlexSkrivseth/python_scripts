
test = [1,2,3,4,5,7]


def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
    elif len(A) == 1:
        return 1

    A.sort()
    for index, num in enumerate(A):
        if index+1 == len(A):
            return 1

        if A[index+1] != num+1:
            return num+1


print(solution(test))
