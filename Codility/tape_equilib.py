def solution1(A):
    # write your code in Python 3.6
    diffs = []
    for index, num in enumerate(A):
        if index+1 < len(A):
            part1 = A[:index+1]
            part2 = A[index+1:]

            abs_diff = abs(sum(part1) - sum(part2))
            diffs.append(abs_diff)


    return min(diffs)


def solution2(A):
    # write your code in Python 3.6
    total = sum(A)

    goal = total/2
    tally = 0
    for index, num in enumerate(A):
        tally += num
        if tally >= goal:

            part1 = A[:index]
            part2 = A[index:]
            possibility1 = abs(sum(part1)-sum(part2))
            possibility2 = abs(tally - total)


            if possibility1 < possibility2 or possibility2 == 0:
                return possibility1
            else:
                return possibility2
