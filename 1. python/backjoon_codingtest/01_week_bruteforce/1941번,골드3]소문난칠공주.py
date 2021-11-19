def new_members(arr,node):
    x,y = arr[node]
    new_member_list = []
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx = x + dx; ny = y + dy
        if 0<=nx<=4 and 0<=ny<=4:
            if (nx,ny) in arr:
                continue
            else:
                new_member_list.append((nx,ny))
    return new_member_list


def backtracing(arr, index, S, Y):
    global answer_set
    global maps
    # 임도연파가 4명 이상인 경우, 제외
    if Y > 3:
        return
    
    # 이다솜파가 4명이상 포함된 칠공주 조합이 생성된 경우 answer_set에 추가
    if index==7:
        arr.sort()
        answer_set.add(tuple(arr))
    else:
        for node in range(len(arr)):
            for new_member in new_members(arr,node):
                nx,ny = new_member
                if maps[nx][ny]=="S":
                    backtracing(arr + [(nx,ny)], index+1, S+1, Y)
                else:
                    backtracing(arr + [(nx,ny)], index+1, S, Y+1)


import sys
answer_set = set()
inputs = sys.stdin.readline
maps = [inputs().strip() for _ in range(5)]
if __name__=="__main__":
    for i in range(5):
        for j in range(5):
            if maps[i][j]=="S":
                backtracing([(i,j)], index=1, S=1, Y=0)
    print(len(answer_set))


# 모든 위치에서 출발하여 확인된 결과를 출력할 수 있지만, time error가 발생할 것으로 판단됨
# dfs보단 backtracing이 적합할 것으로 판단 : 꼬리가 이어지는 형태가 아닌, 아무렇게나 7명이 모이면 되기 때문
# 따라서, S(이다솜파)가 위치한 좌표를 기준으로 탐색하며, backtracing 방법을 활용하되, 만약 Y(임도연파)가 4명 이상인 경우 가지치기