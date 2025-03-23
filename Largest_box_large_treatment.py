def max_volume(X, Y):
    max_a = min(X // 2, Y // 2)
    
    if max_a <= 0:
        return 0
    
    a = 12
    b = -4 * (X + Y)
    c = X * Y
    
    delta = b * b - 4 * a * c
    
    if delta >= 0:
        a1 = (-b + (delta ** 0.5)) / (2 * a)
        a2 = (-b - (delta ** 0.5)) / (2 * a)
    else:
        a1 = a2 = max_a / 2
    
    candidates = [max(1, int(a1)), int(a1) + 1, max(1, int(a2)), int(a2) + 1]
    candidates = [a for a in candidates if 1 <= a <= max_a]
    
    candidates.append(1)
    if max_a > 1:
        candidates.append(max_a)
    
    candidates = list(set(candidates))
    
    max_vol = 0
    for a in candidates:
        vol = (X - 2 * a) * (Y - 2 * a) * a
        max_vol = max(max_vol, vol)
    
    return max_vol

X, Y = map(int, input().split())
print(max_volume(X, Y))