def draw_stars(n):
    if n == 3:
        Map[0][:] = ["*"]*3
        Map[1][:] = ["*"," ","*"]
        Map[2][:] = ["*"]*3
        return
    
    draw_stars(n//3)
    nn = n//3
    for i in range(3):
        for j in range(3):
            if (i==1 and j==1) or (i==0 and j==0):
                continue

            for k in range(nn):
                Map[nn*i+k][nn*j:nn*(j+1)] = Map[k][:nn]


N = int(input())
Map = [[" " for _ in range(N)] for _ in range(N)]

draw_stars(N)
for m in Map:
    print(''.join(m))
