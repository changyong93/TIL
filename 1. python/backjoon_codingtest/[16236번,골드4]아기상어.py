inputs_iter = iter([
#     # ["3", "0 0 0","0 0 0","0 9 0"], #case 1 0
#     # ["3", "0 0 1","0 0 0","0 9 0"], #case 2 3
    ["4","4 3 2 1","0 0 0 0","0 0 9 0","1 2 3 4"], #case 3 14
#     # ["6", "5 4 3 2 3 4","4 3 2 3 4 5","3 2 9 5 6 6","2 1 2 3 4 5","3 2 1 6 5 4","6 6 6 6 6 6"], #case 4 60
#     # ["6", "6 0 6 0 6 1","0 0 0 0 0 2","2 3 4 5 6 6","0 0 0 0 0 2","0 2 0 0 0 0","3 9 3 0 0 1"], #case 5 48
#     ['6',"1 1 1 1 1 1","2 2 6 2 2 3","2 2 5 2 2 3","2 2 2 4 6 3","0 0 0 0 0 6","0 0 0 0 0 9"]# case 6 39
])
input_iter = iter(next(inputs_iter))
# #######################################################################################################################

import sys
from collections import deque

def bfs(x,y,shark,eat_cnt,time):
    p=[[-1]*N for _ in range(N)] #현재 아기 상어 기준 이동할 수 있는 경로를 -1로 한다.
    p[x][y] = time #현재 아기 상어 위치에 time을 저장
    q = deque([(x,y,time)]) 
    result = [] #아기 상어가 먹을 물고기 후보군을 저장
    while q:
        x,y,_ = q.popleft()
        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]: #이동할 다음 위치를 for loop
            nx,ny = x+dx, y+dy #다음 위치 후보
            if 0<=nx<N and 0<=ny<N and p[nx][ny]==-1 and maps[nx][ny]<=shark: #다음 위치가 이동 가능하며 해당 위치의 물고기 크기가 shark보다 작을 때
                p[nx][ny] = p[x][y]+1 #다음 뒤치에 시간 정보 입력
                if maps[nx][ny] == 0 or maps[nx][ny]==shark: #만약 이동 위치에 물고기가 없거나(0) 상어와 크기가 같은 물고기면 다시 loop (이동경로)
                    q.append([nx,ny,p[nx][ny]])
                else: 
                    result.append((nx,ny,p[nx][ny])) #아기상어보다 작은 물고기면 먹을 후보에 저장
    
    if result: #먹을 물고기가 있는 경우
        x,y,time = sorted(result,key = lambda x : [x[2],x[0],x[1]])[0] #물고기의 위치까지 이동 시간, 상하 위치, 좌우 위치 기준으로 sorting하여 먹을 물고기 위치 및 시간 지정
        eat_cnt +=1 #물고기 먹은 횟수 업데이트
        if shark == eat_cnt: #상어 크기와 물고기 먹을 횟수가 같으면 크기 조정 및 먹은 횟수 초기화
            shark +=1
            eat_cnt = 0
        maps[x][y] = 0 #물고기를 먹었으니 해당 위치는 아무것도 없는 0으로 지정
        return x,y,shark,eat_cnt,time
    else: #먹을 물고기가 없는 경우 시간을 반환하고 전체 시스템 종료
        print(time)
        sys.exit()
    
# N = int(sys.stdin.readline())
# maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
N = int(next(input_iter))
maps = [list(map(int, loc.split())) for loc in input_iter]


#maps의 index 기준으로 for loop하여
#아기상어(9)가 있으면 위치를 x,y, maps의 아기상어 위치에 0을 넣고 loop 종료
for i, idx in enumerate(maps):
        try: 
            x,y = i, idx.index(9)
            maps[x][y] = 0
            break
        except ValueError: pass

shark, time, eat_cnt = 2,0,0 #상어 크기, 시간, 물고기 먹은 횟수를 해당 변수에 할당
while True:
    x,y,shark,eat_cnt,time = bfs(x,y,shark,eat_cnt,time) #bfs로 시작!