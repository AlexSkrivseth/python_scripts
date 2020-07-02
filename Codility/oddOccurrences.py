
test_list2 = [ 2, 3, 5, 4, 5, 2, 90, 4, 3, 5, 2, 4, 4, 2, 5]


def solution(N):
    odd_item = False
    for index, i in enumerate(N):
        if i not in N[:index] and i not in N[index + 1:]:
            odd_item = i
    return odd_item

def solution2(A):
    missing_int = 0
    for value in A:
        missing_int ^= value
        print(missing_int)
    return missing_int



def getOddOccurrence(arr):
    # Initialize result
    res = 0
    # Traverse the array
    print(bin(res))
    for element in arr:
        # XOR with the result
        print("XOR COMPARING THESE TWO BITS")
        print(bin(res))
        print(bin(element))
        print("XOR COMPARING THESE TWO BITS")
        res = res ^ element
        print(bin(res))
        print('\n'*5)
    return res


print(getOddOccurrence(test_list2))

print("YOU PASSED HOSER!!!")
