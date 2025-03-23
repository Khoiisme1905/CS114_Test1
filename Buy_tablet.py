import math

d = int(input())

def count_possible_case(diagonal):
    count = 0
    limit = math.isqrt(diagonal**2 // 2) + 1
    d_square = diagonal**2
    for wide in range(1, limit-1):
        l_square = d_square - wide**2
        if l_square > 0:
            l_int = math.isqrt(l_square)
            if l_square == l_int*l_int  and l_int > wide:
                count += 1
    return count


print(count_possible_case(d))