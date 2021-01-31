#백준 15686 치킨 배달 / 1시간 20분
# 첫번째 풀이(주석친부분) : 거리 지도를 만든다 . 치킨집은 거리를 0으로 설정하고 다익스트라로 거리지도를 완성한다.
# 그후 집이있는 위치의 거리를 거리지도를 참조해 구한다.  -> 시간초과
# 어차피 지도가 N*N , N<50 즉 2500번 연산이어서 시간이 남을줄알고 했는데 초과남.

#두번째 풀이 : 조합으로 고른 치킨집을 집과 이중 for문을 돌려서 각집마다 최소 거리를 구하고 총합을 구한다.

#컴비네이션 이후 시간복잡도
#최악의경우 첫번째풀이 :  N^2*M  하지만 계산을 거듭하면 평균 연산수는 제곱에 비례해 줄어들것임..
#최악의경우 두번째 풀이 : 2N*M -> 왜냐면 집의 최대갯수가 2N으로 제한되었기 때문,, 이걸간과했음

#만일 집의 갯수제한이 없었다면  첫번째 풀이가 두번째 풀이보다 빨랐을것 같음
# 왜냐면 최악의경우 두번째풀이는 N*2*M연산을 무조건 해야하지만
# 첫번째 풀이는 연산수가 늘어날수록 연산할 넓이가 매우줄어듬 또한 치킨집의 갯수(M)가 충분히 많은경우도 더 빠를것같음

from itertools import combinations

N, M = map(int, input().split())
ma=[[-1]*(N+2)]
for i in range(N):
    ma.append([-1]+list(map(int, input().split()))+[-1])

chs=[]
zs=[]
ans=100
for i in range(1,N+1):
    for j in range(1,N+1):
        if ma[i][j]==1:
            zs.append([j,i])
        elif ma[i][j]==2:
            chs.append([j,i])

# from copy import deepcopy
# dis=[[-1]*(N+2)]+[[-1]+[100]*N+[-1] for i in range(N)]+[[-1]*(N+2)]
#
# #동남서북
# dx=[1,0,-1,0]
# dy=[0,-1,0,1]
#
# def spread(x,y,k):
#     cdis[y][x]=k
#     for i in range(4):
#         if cdis[y+dy[i]][x+dx[i]]>k+1:
#             spread(x+dx[i],y+dy[i],k+1)
#
# combi = list(combinations(chs,M))
# cdis=[]
# for cch in combi:
#     cdis = deepcopy(dis)
#     for ch in cch:
#         spread(ch[0],ch[1],0)
#     cd=0
#     for z in zs:
#         cd+=cdis[z[1]][z[0]]
#     ans=min(ans,cd)
# print(ans)

combi = list(combinations(chs,M))

for cch in combi:
    cd=0
    for z in zs:
        cur=100
        for ch in cch:
            cur=min(cur,abs(ch[0]-z[0])+abs(ch[1]-z[1]))
        cd+=cur

    ans=min(ans,cd)
print(ans)