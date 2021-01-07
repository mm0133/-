#백준 13458 시험감독/ 13분
N=int(input())
A=list(map(int, input().split()))
B,C= map(int, input().split())
su=N
for i in range(N):
    A[i]-=B+1
    if A[i]>=0:
        tem= (A[i])//C+1
        su+=tem
print(su)

