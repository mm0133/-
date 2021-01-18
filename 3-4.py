#백준 14890 경사로 /1시간 1분  #뭔가 아쉽다. 코드를 깔끔하게 못짬.
#추가: 다른사람 코드 참조시 행만 탐방하는 코드를 짜고 맵을 돌리고 다시한번 행탐밤하는 방법도 있다!
# 다른방법 왼쪽과 오른쪽이같을때 cnt+=1  왼쪽이 오른쪽보다 작으면 cnt>L인지 확인  오른쪽이 왼쪽보다 작으면 cnt=-L 불연속(혹은 끝)만나면 cnt>0인지 체크
#pypy3 6등/240명
N,L=map(int,input().split())
ma=[]

for i in range(N):
    ma.append(list(map(int,input().split())))
count=0
dx=[1,0]
dy=[0,1]

for i in range(N):
    f=0
    vi = [0] * N
    for k in range(N-1):

        if abs(ma[i][k]-ma[i][k+1])>1:
            f=1
            break
        elif ma[i][k]-ma[i][k+1]==1:
            if k+L<N:
                ck=0
                for l in range(L):
                    if ma[i][k+l+1]!=ma[i][k+1] or vi[k+l+1]:
                        ck=1
                        break
                    else:
                        vi[k+l+1] = 1
                if ck:
                    f=1
                    break
            else:
                f=1
                break

        elif ma[i][k+1]-ma[i][k]==1:
            if k+1-L>=0:
                ck = 0
                for l in range(L):
                    if ma[i][k-l] != ma[i][k] or vi[k-l]:
                        ck = 1
                        break
                    else:
                        vi[k - l]=1
                if ck:
                    f=1
                    break
            else:
                f=1
                break
    if not f:
        count+=1

for i in range(N):
    f = 0
    vi = [0] * N
    for k in range(N - 1):
        if abs(ma[k][i] - ma[k+1][i]) > 1:
            f = 1
            break
        elif ma[k][i] - ma[k+1][i] == 1:
            if k + L < N:
                ck = 0
                for l in range(L ):
                    if ma[k + l + 1][i] != ma[k+1][i] or vi[k + l + 1]:
                        ck = 1
                        break
                    else:
                        vi[k + l + 1]=1
                if ck:
                    f = 1
                    break
            else:
                f=1
                break

        elif ma[k+1][i] - ma[k][i] == 1:
            if k + 1 - L >= 0:
                ck = 0
                for l in range(L ):
                    if ma[k-l][i] != ma[k][i] or vi[k - l]:
                        ck = 1
                        break
                    else:
                        vi[k - l]=1
                if ck:
                    f = 1
                    break
            else:
                f=1
                break
    if not f:
        count += 1

print(count)