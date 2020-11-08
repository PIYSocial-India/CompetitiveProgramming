n = int(input())
cnt = 0
l = [int(i) for i in input().split()]

for i in range(1,n):
    if l[i] < l[i-1]:
        cnt = cnt + (l[i-1] - l[i])
        l[i] = l[i-1]

print(cnt)