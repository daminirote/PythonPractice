
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(arr)
leftSum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            leftSum +=arr[i][j]
print(leftSum)

k = 0
l = n-1
rightSum = 0
while(l>=0 and k<= n):
    rightSum = rightSum + arr[k][l]
    k+=1
    l-=1
print(rightSum)
