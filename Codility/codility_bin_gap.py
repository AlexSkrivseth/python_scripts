test_nums = [120, 0, 1, 1234567890, 2147483647, 78]
test_num = 1234567890
# 1001001100101100000001011010010

def solution(N):
    if N in range(1,2147483647):
        binary = bin(N)[2:]
        gaps = [0]
        for index, i in enumerate(binary):

            if i == '0' and index != '0':

                count = 0
                for j in binary[index:]:

                    if j == '0':

                        count += 1
                    else:
                        gaps.append(count)
                        break
        return max(gaps)

    else:
        return "N not in range"
