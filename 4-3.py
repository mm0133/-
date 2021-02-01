#백준 15685 드래곤커브 /1시간 40분
# 아.... 이거 정사각형 네변 모두 칠해진거인줄 알았는데 ...네귀퉁이가 칠해진거였네 ...
# 문제좀 꼼꼼꼼꼼꼼꼼꼼꼼히 읽자 ㅜㅜ 으아ㅜㅜ
#아래 주석된 코드는 네변이 모두 칠해진 정사각형수


# N = int(input())
# dragons=[]
# for i in range(N):
#     dragons.append(list(map(int, input().split())))
#
# ga=[[0]*100 for i in range(101)]
# se=[[0]*101 for i in range(100)]
# #동북서남순
# bix=[0,0,-1,0]
# biy=[0,-1,0,0]
# dx=[1,0,-1,0]
# dy=[0,-1,0,1]
#
# for dg in dragons:
#     dvt =[dg[2]]
#     if dvt[0] %2:
#         se[biy[dvt[0]]+dg[1]][bix[dvt[0]]+dg[0]]=1
#     else:
#         ga[biy[dvt[0]]+dg[1]][bix[dvt[0]]+dg[0]]=1
#
#     x=dg[0]+dx[dvt[0]]
#     y=dg[1]+dy[dvt[0]]
#
#     g=0
#     while g<dg[3]:
#
#         a=len(dvt)-1
#         while a>=0:
#             di=(dvt[a]+1)%4
#             dvt.append(di)
#
#             if di % 2:
#                 se[biy[di] + y][bix[di] + x] = 1
#             else:
#                 ga[biy[di] + y][bix[di] + x] = 1
#
#             x+=dx[di]
#             y+=dy[di]
#             a-=1
#
#         g+=1
#
# cnt=0
# for i in range(100):
#     for j in range(100):
#         if ga[i][j] and ga[i+1][j] and se[i][j] and se[i][j+1]:
#             cnt+=1
#
# print(cnt)



N = int(input())
dragons=[]
for i in range(N):
    dragons.append(list(map(int, input().split())))

ma=[[0]*101 for i in range(101)]
#동북서남순
dx=[1,0,-1,0]
dy=[0,-1,0,1]

for dg in dragons:
    dvt =[dg[2]]

    x=dg[0]+dx[dvt[0]]
    y=dg[1]+dy[dvt[0]]
    ma[dg[1]][dg[0]]=1
    ma[y][x]=1
    g=0
    while g<dg[3]:
        a=len(dvt)-1
        while a>=0:
            di=(dvt[a]+1)%4
            dvt.append(di)
            x+=dx[di]
            y+=dy[di]
            ma[y][x]=1
            a-=1

        g+=1

cnt=0
for i in range(100):
    for j in range(100):
        if ma[i][j] and ma[i+1][j] and ma[i+1][j+1] and ma[i][j+1]:
            cnt+=1
print(cnt)

