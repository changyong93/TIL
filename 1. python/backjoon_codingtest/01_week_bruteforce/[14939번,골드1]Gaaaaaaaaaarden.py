import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def get_location(x,y, maps):
    location_list = []
    for dx,dy in dirs:
        nx = x+dx ; ny= y+dy
        if 0<=nx<=N-1 and 0<=ny<=M-1:
            if maps[nx][ny] == 1 or maps[nx][ny] == 2:
                location_list.append((nx,ny))
    return location_list


def bfs(maps, red,selected):
    cnt = 0
    red_q = deque()
    green_q = deque()

    for x,y in selected:
        if (x,y) in red:
            red_q.append((x,y)) #빨강색 배양액
            maps[x][y] = 3
        else:
            green_q.append((x,y)) #초록색 배양액
            maps[x][y] = 4
    
    # 빨간색 및 초록색 배양액이 남은 경우 진행
    while red_q and green_q:
        red_tmp = set()
        green_tmp = set()
        
        #현재 빨강색 배양액 위치에서 퍼지는 위치 탐색
        while red_q:
            x,y = red_q.popleft()
            red_tmp.update(get_location(x,y,maps))
        
        #현재 초록색 배양액 위치에서 퍼지는 위치 탐색
        while green_q:
            x,y = green_q.popleft()
            green_tmp.update(get_location(x,y,maps))

        # 꽃 (= 동일 시간대의 빨강색 및 초록색 배양액이 겹친 위치)
        inter = red_tmp & green_tmp

        # 빨강색 배양액
        red_tmp = red_tmp - inter
        # 초록색 배양액
        green_tmp = green_tmp - inter

        # 현재 시점에서 배양액 혹은 꽃의 위치 표시
        for x,y in inter:
            maps[x][y] = 5
            cnt +=1
        for x,y in red_tmp:
            maps[x][y] = 3
        for x,y in green_tmp:
            maps[x][y] = 4

        #다음 배양액이 퍼지는 위치 탐색을 위한 현재 위치 추가
        red_q.extend(red_tmp)
        green_q.extend(green_tmp)
        
    return cnt


inputs = sys.stdin.readline
if __name__=="__main__":
    N, M, R, G = map(int, inputs().strip().split(" "))
    maps = [list(map(int, inputs().strip().split(" "))) for _ in range(N)]
    answer = 0
    
    #배양액을 뿌릴 수 있는 땅 위치 탐색
    locations = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]==2:
                locations.append((i,j))

    #배양액을 뿌릴 수 있는 땅에서, 초록색 배양액과 빨간색 배양액 위치 나누기
    for selected in combinations(locations, R+G):
        for red in combinations(selected, R):
            tmp_maps = deepcopy(maps)
            answer = max(answer,bfs(tmp_maps, red,selected))
    print(answer)
                
            
    