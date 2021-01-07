N, M = map(int, input().split())
bo = [[0]*M for i in range(N)]
R = [0, 0]
B = [0, 0]
O = [0, 0]
cl=-1
check = 0
for i in range(N):
    tem = input()
    for j in range(M):
        bo[i][j] = tem[j]
        if tem[j] == 'R':
            R = [i, j]
        if tem[j] == 'B':
            B = [i, j]
        if tem[j] == 'O':
            O = [i, j]

qu = [(R, B, 0)]


while qu:
    cur=qu.pop(0)
    if cur[2] == 10:
        break
    CR = cur[0]
    CB = cur[1]
    AR=CR.copy()
    AB=CB.copy()
    checkR=0
    checkB=0

    if CR[1] - CB[1] == 1:
        while not (((bo[AR[0]][AR[1] - 1] == '#' or (AR[0] == AB[0] and AR[1] - 1 == AB[1])) or checkR) and (
                bo[AB[0]][AB[1] - 1] == '#' or (AB[0] == AR[0] and AB[1] - 1 == AR[1]))):

            if bo[AB[0]][AB[1] - 1] == 'O':
                checkB = 1
                break
            if not (bo[AB[0]][AB[1] - 1] == '#' or (AB[0] == AR[0] and AB[1] - 1 == AR[1])):
                AB[1] = AB[1] - 1

            if not ((bo[AR[0]][AR[1] - 1] == '#' or (AR[0] == AB[0] and AR[1] - 1 == AB[1])) or checkR):
                if bo[AR[0]][AR[1] - 1] == 'O':
                    checkR = 1
                    AR=[-1,-1]

                AR[1] = AR[1] - 1

    else:
        while not (((bo[AR[0]][AR[1] - 1] == '#' or (AR[0] == AB[0] and AR[1] - 1 == AB[1])) or checkR) and (
                bo[AB[0]][AB[1] - 1] == '#' or (AB[0] == AR[0] and AB[1] - 1 == AR[1]))):

            if not((bo[AR[0]][AR[1] - 1] == '#' or (AR[0] == AB[0] and AR[1] - 1 == AB[1])) or checkR):
                if bo[AR[0]][AR[1] - 1] == 'O':
                    checkR = 1
                    AR=[-1,-1]
                AR[1] = AR[1] - 1

            if bo[AB[0]][AB[1] - 1] == 'O':
                checkB = 1
                break
            if not (bo[AB[0]][AB[1] - 1] == '#' or (AB[0] == AR[0] and AB[1] - 1 == AR[1])):
                AB[1] = AB[1] - 1


    if checkR and not checkB:
        cl=cur[2]+1
        break
    if (not checkB) and (AR!=CR or AB!=CB):
        qu.append((AR,AB,cur[2]+1))

    AR=CR.copy()
    AB=CB.copy()
    checkR=0
    checkB=0


    if CR[1] - CB[1] == -1:
        while not (((bo[AR[0]][AR[1] + 1] == '#' or (AR[0] == AB[0] and AR[1] + 1 == AB[1])) or checkR) and (
                bo[AB[0]][AB[1] + 1] == '#' or (AB[0] == AR[0] and AB[1] + 1 == AR[1]))):

            if bo[AB[0]][AB[1] + 1] == 'O':
                checkB = 1
                break
            if not (bo[AB[0]][AB[1] + 1] == '#' or (AB[0] == AR[0] and AB[1] + 1 == AR[1])):
                AB[1] = AB[1] + 1

            if not ((bo[AR[0]][AR[1] + 1] == '#' or (AR[0] == AB[0] and AR[1] + 1 == AB[1])) or checkR):
                if bo[AR[0]][AR[1] + 1] == 'O':
                    checkR = 1
                    AR = [-1, -1]
                AR[1] = AR[1] + 1
    else:
        while not (((bo[AR[0]][AR[1] + 1] == '#' or (AR[0] == AB[0] and AR[1] + 1 == AB[1])) or checkR) and (
                bo[AB[0]][AB[1] + 1] == '#' or (AB[0] == AR[0] and AB[1] + 1 == AR[1]))):

            if not ((bo[AR[0]][AR[1] + 1] == '#' or (AR[0] == AB[0] and AR[1] + 1 == AB[1])) or checkR):
                if bo[AR[0]][AR[1] + 1] == 'O':
                    checkR = 1
                    AR = [-1, -1]
                AR[1] = AR[1] + 1
            if bo[AB[0]][AB[1] + 1] == 'O':
                checkB = 1
                break
            if not (bo[AB[0]][AB[1] + 1] == '#' or (AB[0] == AR[0] and AB[1] + 1 == AR[1])):
                AB[1] = AB[1] + 1

    if checkR and not checkB:
        cl=cur[2]+1
        break
    if (not checkB) and (AR!=CR or AB!=CB):
        qu.append((AR,AB,cur[2]+1))

    AR=CR.copy()
    AB=CB.copy()
    checkR=0
    checkB=0

    if CR[0] - CB[0] == 1:
        while not (((bo[AR[0]-1][AR[1]] == '#' or (AR[0]-1 == AB[0] and AR[1] == AB[1])) or checkR) and (
                bo[AB[0]-1][AB[1]] == '#' or (AB[0]-1 == AR[0] and AB[1] == AR[1]))):

            if bo[AB[0]-1][AB[1]] == 'O':
                checkB = 1
                break
            if not (bo[AB[0]-1][AB[1]] == '#' or (AB[0]-1 == AR[0] and AB[1]== AR[1])):
                AB[0] = AB[0] - 1

            if not ((bo[AR[0]-1][AR[1]] == '#' or (AR[0]-1 == AB[0] and AR[1]== AB[1])) or checkR):
                if bo[AR[0]-1][AR[1]] == 'O':
                    checkR = 1
                    AR = [-1, -1]
                AR[0] = AR[0] - 1

    else:
        while not (((bo[AR[0]-1][AR[1]] == '#' or (AR[0]-1 == AB[0] and AR[1] == AB[1])) or checkR) and (
                bo[AB[0]-1][AB[1]] == '#' or (AB[0]-1 == AR[0] and AB[1] == AR[1]))):

            if not ((bo[AR[0]-1][AR[1]] == '#' or (AR[0]-1 == AB[0] and AR[1] == AB[1])) or checkR):
                if bo[AR[0]-1][AR[1]] == 'O':
                    checkR = 1
                    AR = [-1, -1]
                AR[0] = AR[0] - 1

            if bo[AB[0]-1][AB[1]] == 'O':
                checkB = 1
                break
            if not (bo[AB[0]-1][AB[1]] == '#' or (AB[0]-1 == AR[0] and AB[1]  == AR[1])):
                AB[0] = AB[0] - 1


    if checkR and not checkB:
        cl=cur[2]+1
        break
    if (not checkB) and (AR!=CR or AB!=CB):
        qu.append((AR,AB,cur[2]+1))

    AR=CR.copy()
    AB=CB.copy()
    checkR=0
    checkB=0



    if CR[0] - CB[0] == -1:
        while not (((bo[AR[0] + 1][AR[1]] == '#' or (AR[0] + 1 == AB[0] and AR[1] == AB[1])) or checkR) and (
                bo[AB[0] + 1][AB[1]] == '#' or (AB[0] + 1 == AR[0] and AB[1] == AR[1]))):

            if bo[AB[0] + 1][AB[1]] == 'O':
                checkB = 1
                break
            if not (bo[AB[0] + 1][AB[1]] == '#' or (AB[0] + 1 == AR[0] and AB[1] == AR[1])):
                AB[0] = AB[0] + 1

            if not ((bo[AR[0] + 1][AR[1]] == '#' or (AR[0] + 1 == AB[0] and AR[1] == AB[1])) or checkR):
                if bo[AR[0] + 1][AR[1]] == 'O':
                    checkR = 1
                    AR = [-1, -1]
                AR[0] = AR[0] + 1

    else:
        while not (((bo[AR[0] + 1][AR[1]] == '#' or (AR[0] + 1 == AB[0] and AR[1] == AB[1])) or checkR) and (
                bo[AB[0] + 1][AB[1]] == '#' or (AB[0] + 1 == AR[0] and AB[1] == AR[1]))):

            if not ((bo[AR[0] + 1][AR[1]] == '#' or (AR[0] + 1 == AB[0] and AR[1] == AB[1])) or checkR):
                if bo[AR[0] + 1][AR[1]] == 'O':
                    checkR = 1
                    AR = [-1, -1]
                AR[0] = AR[0] + 1

            if bo[AB[0] + 1][AB[1]] == 'O':
                checkB = 1
                break
            if not (bo[AB[0] + 1][AB[1]] == '#' or (AB[0] + 1 == AR[0] and AB[1] == AR[1])):
                AB[0] = AB[0] + 1

    if checkR and not checkB:
        cl=cur[2]+1
        break

    if (not checkB) and (AR!=CR or AB!=CB):
        qu.append((AR,AB,cur[2]+1))

print(cl)

#3시간 31분