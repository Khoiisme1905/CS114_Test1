#Nhap phieu
phieu = []
for _ in range(3):
    phieu.append(list(map(int, input().split())))


N = int(input())
so_rut = []
for _ in range(N):
    so_rut.append(int(input()))

#Tao mang de check
mark = [[False]*3 for i in range(3)]

for i in range(3):
    for j in range(3):
        if phieu[i][j] in so_rut:
            mark[i][j] = True

#Ham check loto
def check(m):
    #Check hang
    for i in range(3):
        if mark[i] == [True, True, True]:
            return True
    #Check cot
    for j in range(3):
        if mark[0][j] and mark[1][j] and mark[2][j]:
            return True
    #Check duong cheo
    if mark[0][0] and mark[1][1] and mark[2][2]:
        return True
    if mark[0][2] and mark[1][1] and mark[2][0]:
        return True
    return False

if check(mark):
    print("Yes")
else:
    print("No")