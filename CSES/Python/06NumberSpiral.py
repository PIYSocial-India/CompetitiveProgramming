n = int(input())

l = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    y,x = l[i][0] , l[i][1]

    if x>y:
        if x%2 == 1:
            print(x*x - y + 1)
        else:
            x-=1
            print(x*x + y)
    else:
        if y%2 == 0:
            print(y*y - x + 1)
        else:
            y-=1
            print(y*y + x)