#백준 14503 로봇청소기 /1시간 22분
#  실수로 row column 바까서 생각함... 덕분에  40분만에 푼거 40분 추가로 더걸림..  정신좀 차리자..
#pypy3기준 숏코딩 6등/363명, 시간 54등/363명
N,M=map(int,input().split())
fr,fc,fd=map(int,input().split())

ma=[]
for i in range(N):
    ma.append(list(map(int,input().split())))

#0 1 2 3 북 동 남 서
dr=[0,1,0,-1]
dc=[-1,0,1,0]
cnt=1
ma[fr][fc]=2

def dfs(r,c,d):
    nd=d
    for i in range(4):
        nd=(nd-1)%4
        if ma[c+dc[nd]][r+dr[nd]]==0:
            ma[c + dc[nd]][r + dr[nd]]=2
            global cnt
            cnt+=1

            dfs(r+dr[nd],c+dc[nd],nd)
            return

    if ma[c - dc[nd]][r - dr[nd]]!=1:
        dfs( r - dr[nd],c - dc[nd], nd)
    return

dfs(fc,fr,fd)

print(cnt)