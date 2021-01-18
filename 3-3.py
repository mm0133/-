#백준 14889 스타트링크 /48분
#pypy3 17등/738명
N= int(input())
su=0
S=[]
for i in range(N):
    S.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        su+=S[i][j]
sub=20*20*100


def dfs(t1,x):
    if x==N//2:

        global sub
        t2=[]
        for i in range(N):
            if not i in t1:
                t2.append(i)

        t1s=get_grade(t1)
        t2s=get_grade(t2)
        sub=min(abs(t1s-t2s),sub)
        return

    for i in range(t1[-1]+1 , N//2+x+1):
        nt1=t1[:]
        nt1.append(i)
        dfs(nt1,x+1)

def get_grade(t):
    su=0
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
            su=su+S[t[i]][t[j]]+S[t[j]][t[i]]
    return su

dfs([0],1)
print(sub)






