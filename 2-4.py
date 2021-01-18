# 백준 14502 연구소 /1시간 1분
N, M = map(int, input().split())
ma = []
tmpma = [[0] * M for _ in range(N)]
for i in range(N):
    ma.append(list(map(int, input().split())))
vir = []
for i in range(N):
    for j in range(M):
        if ma[i][j] == 2:
            vir.append((j, i))
anw = 0


def spread(m):
    stack = vir.copy()
    while (stack):
        x = stack[-1][0]
        y = stack[-1][1]
        stack.pop()
        if x > 0:
            if m[y][x - 1] == 0:
                m[y][x - 1] = 2
                stack.append((x - 1, y))
        if x < M - 1:
            if m[y][x + 1] == 0:
                m[y][x + 1] = 2
                stack.append((x + 1, y))

        if y > 0:
            if m[y - 1][x] == 0:
                m[y - 1][x] = 2
                stack.append((x, y - 1))
        if y < N - 1:
            if m[y + 1][x] == 0:
                m[y + 1][x] = 2
                stack.append((x, y + 1))
    count = 0
    for i in range(N):
        for j in range(M):
            if m[i][j] == 0:
                count += 1
    return count


def go(r1, r2, r3):
    global anw
    for i in range(N):
        for j in range(M):
            tmpma[i][j] = ma[i][j]

    if tmpma[r1 // M][r1 % M] == 0:
        tmpma[r1 // M][r1 % M] = 1
    else:
        return

    if tmpma[r2 // M][r2 % M] == 0:
        tmpma[r2 // M][r2 % M] = 1
    else:
        return

    if tmpma[r3 // M][r3 % M] == 0:
        tmpma[r3 // M][r3 % M] = 1
    else:
        return

    anw = max(anw, spread(tmpma))


for i in range(N * M - 2):
    for j in range(i + 1, N * M - 1):
        for k in range(j + 1, N * M):
            go(i, j, k)

print(anw)
