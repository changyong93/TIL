inputs_iter = iter([
    ["5 4","0 0 1 0","0 0 0 0","1 0 0 0","0 0 0 0","0 0 0 1"],
    # ["7 4","0 0 0 1","0 1 0 0","0 0 0 0","0 0 0 1","0 0 0 0","0 1 0 0","0 0 0 1"],
    # ["5 6","1 0 1 0 0 0","0 0 0 0 0 0","0 0 0 0 0 0","0 0 0 0 0 0","0 0 0 0 0 0"]
])
input_iter = iter(next(inputs_iter))
#######################################################################################################################
import sys
from collections import deque

n,m = map(int,next(input_iter).split())
# n,m = map(int, sys.stdin.readline().split())

sharks=deque()
safe_dist = []

for i in range(n): #행 기준으로 데이터 가져옴
    tmp = list(map(int,next(input_iter).split()))
    # tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m): #열 element값 중에서 shark(1)이 있으면 해당 값 sharks에 저장
        if tmp[j] == 1:
            sharks.append((i,j))
    safe_dist.append(tmp)

xs = [-1, -1, -1, 0, 1, 0, 1, 1]
ys = [-1, 0, 1, 1, 1, -1, 0, -1]
while sharks:
    x,y = sharks.popleft()
    for dx,dy in zip(xs,ys):
        nx,ny = x+dx, y+dy
        if 0<=nx<=n-1 and 0<=ny<=m-1: #shark의 이동 경로가 범위 내에 있는지
            if safe_dist[nx][ny]==0: #이동 경로를 다른 상어가 이동하지 않은 경우 이동
                safe_dist[nx][ny] = safe_dist[x][y]+1
                sharks.append((nx,ny))

print(max(sum(safe_dist,[]))-1) #safe_dist거리를 구한게 2중 list이므로 sum으로 합쳐준 후 최종 값에서 1 반환