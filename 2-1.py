#백준 14499 주사위 굴리기 / 1시간 16분
N, M, y, x, k =map(int,input().split())
bo=[]
for i in range(N):
    bo.append(list(map(int,input().split())))

inst=list(map(int,input().split()))
state=[0,0,0,0,0,0]

# 1동 2 서 3 북 4 남

def turn(dir):
    global state,x,y
    tem = state.copy()

    if dir==1:
        if x==M-1:
            return False
        x+=1
        if bo[y][x]:
            tem[0]=bo[y][x]
            bo[y][x]=0
        else:
            tem[0] = state[4]
            bo[y][x]= state[4]
        tem[3]=state[0]
        tem[4]=state[5]
        tem[5]=state[3]
    elif dir==2:
        if x==0:
            return False
        x -= 1
        if bo[y][x]:
            tem[0]=bo[y][x]
            bo[y][x]=0
        else:
            tem[0] = state[3]
            bo[y][x]= state[3]

        tem[3]=state[5]
        tem[4]=state[0]
        tem[5]=state[4]
    elif dir==3:
        if y==0:
            return False
        y -= 1
        if bo[y][x]:
            tem[0]=bo[y][x]
            bo[y][x]=0
        else:
            tem[0] = state[1]
            bo[y][x]= state[1]
        tem[1]=state[5]
        tem[2]=state[0]
        tem[5]=state[2]
    else:
        if y==N-1:
            return False
        y+=1
        if bo[y][x]:
            tem[0] = bo[y][x]
            bo[y][x] = 0
        else:
            tem[0] = state[2]
            bo[y][x] = state[2]

        tem[1]=state[0]
        tem[2]=state[5]
        tem[5]=state[1]
    state = tem
    return True

for i in inst:
    if turn(i):
        print(state[5])