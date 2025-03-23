def max_volume(X, Y):
    max_vol = 0
    max_a = 0
    for a in range(1, min(X // 2, Y // 2) + 1):
        vol = (X - 2 * a) * (Y - 2 * a) * a
        if vol > max_vol:
            max_vol = vol
            max_a = a
    return max_vol


X, Y = map(int, input().split())


print(max_volume(X, Y))