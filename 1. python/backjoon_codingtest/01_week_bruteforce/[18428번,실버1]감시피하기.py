import sys
from itertools import combinations

def watch(teacher_list,maps,walls,N):
    for teacher in teacher_list:
        for nx,ny in [(-1,0),(1,0),(0,-1),(0,1)]:
            x,y = teacher
            while 0 <= x <= N-1 and 0 <= y <= N-1:
                if maps[x][y] == "S":
                    return False
                if (x,y) in walls:
                    break
                x+=nx; y+=ny
                
    return True


def escape(empty_list,teacher_list,maps,N):
    #벽 3개 뽑기
    for walls in combinations(empty_list,3):
        #탈출 가능한지 확인하기
        if watch(teacher_list,maps,walls, N):
            print("YES")
            return
    print("NO")

inputs = sys.stdin.readline
if __name__=="__main__":
    N = int(inputs())
    maps = [inputs().strip().split() for _ in range(N)]
    
    #빈 공간 및 선생님 위치 확인
    empty_list = []
    teacher_list = []
    for i in range(len(maps)):
        for j in range(len(maps)):
            if maps[i][j] == "T":
                teacher_list.append((i,j))
            elif maps[i][j] == "X":
                empty_list.append((i,j))

    escape(empty_list,teacher_list,maps,N)