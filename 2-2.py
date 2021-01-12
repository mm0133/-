#백준14500 테트로미노 59분
N,M=map(int, input().split())
bo=[]
for i in range(N):
    bo.append(list(map(int,input().split())))

MV=0
arrlist=[]

arr1_1=[[1,1,1,1]]
arr1_2=[[1],[1],[1],[1]]
arr2=[[1,1],
      [1,1]]
arr3=[[1,0],[1,0],[1,1]]
arr3_=[[1,1,1],[1,0,0]]
arr4=[[1,0],[1,1],[0,1]]
arr4_=[[0,1,1],[1,1,0]]
arr5=[[1,1,1],[0,1,0]]
arr5_=[[0,1],[1,1],[0,1]]
arrlist=[arr1_1,arr1_2,arr2,arr3,arr3_,arr4,arr4_,arr5,arr5_]



def rotate(arr):
    y = len(arr)
    x = len(arr[0])

    tem=[[0]*x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            tem[i][j]=arr[y-1-i][x-1-j]
    return tem


def flip(arr):
    y = len(arr)
    x = len(arr[0])
    tem = [[0] * x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            tem[i][j] = arr[i][x - 1 - j]
    return tem


def go(array):
    global MV
    y=len(array)
    x=len(array[0])


    for i in  range(N-y+1):
        for j in range(M-x+1):
            su = 0
            for k in range(y):
                for l in range(x):
                    if array[k][l]:
                        su+=bo[i+k][j+l]
            MV=max(MV,su)




for i in arrlist:
    go(i)
    go(rotate(i))
    j=flip(i)
    go(j)
    go(rotate(j))


print(MV)