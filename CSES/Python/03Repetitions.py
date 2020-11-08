a = list(input())

cnt = 0
x = 0

for i in range(len(a)-1):

    if a[i] == a[i+1]:
        cnt += 1
        if x <= cnt:
            x = cnt
    elif a[i] != a[i+1]:
        cnt = 0

print(x+1)