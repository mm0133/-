# 백준 5373 큐빙 /1시간 44분
U = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
D = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
F = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
B = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
L = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
R = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]


def go(ins):
    if ins == 'U+':
        rotate(1, U, B, R, F, L, 0, 0, 0, 0)
    elif ins == 'U-':
        rotate(0, U, L, F, R, B, 0, 0, 0, 0)
    elif ins == 'D+':
        rotate(1, D, F, R, B, L, 2, 2, 2, 2)
    elif ins == 'D-':
        rotate(0, D, L, B, R, F, 2, 2, 2, 2)
    elif ins == 'F+':
        rotate(1, F, U, R, D, L, 2, 3, 0, 1)
    elif ins == 'F-':
        rotate(0, F, L, D, R, U, 1, 0, 3, 2)
    elif ins == 'B+':
        rotate(1, B, U, L, D, R, 0, 3, 2, 1)
    elif ins == 'B-':
        rotate(0, B, R, D, L, U, 1, 2, 3, 0)
    elif ins == 'L+':
        rotate(1, L, U, F, D, B, 3, 3, 3, 1)
    elif ins == 'L-':
        rotate(0, L, B, D, F, U, 1, 3, 3, 3)
    elif ins == 'R+':
        rotate(1, R, U, B, D, F, 1, 3, 1, 1)
    else:
        rotate(0, R, F, D, B, U, 1, 1, 3, 1)


# 다른면들의 방향 시계 0 반시계 1
# u r d l -> 0 1 2 3
# U -> B R F D  0000
# D -> F R B L  2222
# F -> U R D L  2301
# B -> U L D R  0321
# L -> U F D B  3331
# R -> U B D F  1311

# (r,c)
Di = [[[(0, 0), (0, 1), (0, 2)], [(0, 2), (1, 2), (2, 2)], [(2, 2), (2, 1), (2, 0)], [(2, 0), (1, 0), (0, 0)]],
     [[(0, 2), (0, 1), (0, 0)], [(2, 2), (1, 2), (0, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)]]]


def rotate(ccl, f, x1, x2, x3, x4, d1, d2, d3, d4):
    tmp = [
        x1[Di[ccl][d1][0][0]][Di[ccl][d1][0][1]],
        x1[Di[ccl][d1][1][0]][Di[ccl][d1][1][1]],
        x1[Di[ccl][d1][2][0]][Di[ccl][d1][2][1]],
    ]

    x1[Di[ccl][d1][0][0]][Di[ccl][d1][0][1]] = x4[Di[ccl][d4][0][0]][Di[ccl][d4][0][1]]
    x1[Di[ccl][d1][1][0]][Di[ccl][d1][1][1]] = x4[Di[ccl][d4][1][0]][Di[ccl][d4][1][1]]
    x1[Di[ccl][d1][2][0]][Di[ccl][d1][2][1]] = x4[Di[ccl][d4][2][0]][Di[ccl][d4][2][1]]

    tmp2 = [
        x2[Di[ccl][d2][0][0]][Di[ccl][d2][0][1]],
        x2[Di[ccl][d2][1][0]][Di[ccl][d2][1][1]],
        x2[Di[ccl][d2][2][0]][Di[ccl][d2][2][1]],
    ]

    x2[Di[ccl][d2][0][0]][Di[ccl][d2][0][1]] = tmp[0]
    x2[Di[ccl][d2][1][0]][Di[ccl][d2][1][1]] = tmp[1]
    x2[Di[ccl][d2][2][0]][Di[ccl][d2][2][1]] = tmp[2]
    tmp = [
        x3[Di[ccl][d3][0][0]][Di[ccl][d3][0][1]],
        x3[Di[ccl][d3][1][0]][Di[ccl][d3][1][1]],
        x3[Di[ccl][d3][2][0]][Di[ccl][d3][2][1]],
    ]

    x3[Di[ccl][d3][0][0]][Di[ccl][d3][0][1]] = tmp2[0]
    x3[Di[ccl][d3][1][0]][Di[ccl][d3][1][1]] = tmp2[1]
    x3[Di[ccl][d3][2][0]][Di[ccl][d3][2][1]] = tmp2[2]

    x4[Di[ccl][d4][0][0]][Di[ccl][d4][0][1]] = tmp[0]
    x4[Di[ccl][d4][1][0]][Di[ccl][d4][1][1]] = tmp[1]
    x4[Di[ccl][d4][2][0]][Di[ccl][d4][2][1]] = tmp[2]


    if ccl:
        tmp=f[0][0]
        f[0][0]=f[2][0]
        tmp2=f[0][2]
        f[0][2]=tmp
        tmp=f[2][2]
        f[2][2]=tmp2
        f[2][0]=tmp

        tmp = f[0][1]
        f[0][1] = f[1][0]
        tmp2 = f[1][2]
        f[1][2] = tmp
        tmp = f[2][1]
        f[2][1] = tmp2
        f[1][0] = tmp



    else:
        tmp=f[0][0]
        f[0][0]=f[0][2]
        tmp2=f[2][0]
        f[2][0]=tmp
        tmp=f[2][2]
        f[2][2]=tmp2
        f[0][2]=tmp

        tmp = f[0][1]
        f[0][1] = f[1][2]
        tmp2 = f[1][0]
        f[1][0] = tmp
        tmp = f[2][1]
        f[2][1] = tmp2
        f[1][2] = tmp

TC= int(input())
for t in range(TC):
    U = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    D = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    F = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    B = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    L = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    R = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    N=input()
    ins=input().split()
    for i in ins:
        go(i)
    print(U[0][0] + U[0][1] + U[0][2])
    print(U[1][0] + U[1][1] + U[1][2])
    print(U[2][0] + U[2][1] + U[2][2])