# 백준 14891 톱니바퀴 #일부러 비트연산자로 풀다가 늦음  /1시간 29분
#pypy3  7등/264명
A=[0]
for i in range(4):
    A.append(int(input(),2))


K=int(input())
I=[]
for i in range(K):
    I.append(list(map(int, input().split())))

def rotate(x, dir):
    res=x
    if dir<0:
        if x& 0b10000000:
            res=(res<<1 & 0b11111111) + 0b1
        else:
            res=res<<1
    else:
        if x& 0b1:
            res=(res>>1) + 0b10000000
        else:
            res=res>>1
    return res




for i in I:

    rcheck = [0, 0, 0, 0, 0]
    cur = i[0]
    r= cur+1
    l= cur-1
    rcheck[cur]=i[1]

    while r<5:
        if bool(A[cur]& 0b00100000) ^ bool(A[r]&0b00000010):
            rcheck[r]=-rcheck[cur]
            cur=r
            r+=1
        else:
            r=5
    cur = i[0]

    while l>0:

        if bool(A[l] & 0b00100000) ^ bool(A[cur] & 0b00000010):
            rcheck[l] = -rcheck[cur]
            cur=l
            l-=1
        else:
            l = 0

    for j in range(1,5):
        if rcheck[j]:
            A[j]=rotate(A[j],rcheck[j])


su=0
for i in range(1,5):
    su=su+bool(A[i]&0b10000000)*(0b1<<(i-1))
print(su)