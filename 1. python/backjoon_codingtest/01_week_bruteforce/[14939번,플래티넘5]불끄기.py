"""
1. 모든 스위치를 끄고 켜보면 정답을 구할 수 있음
2. 단 이 경우, 전구가 100개가 존재하므로 시간복잡도는 O(2^(n*n)) = O(2^(10*10)) = O(2^100)
3. 따라서 조건을 단순화 시켜야 함
4. 우선, 간단한 규칙을 정하여, 스위치는 왼쪽 상단부터 오른쪽 하단까지 오른쪽으로 하나씩 전구를 스위치를 누르도록 함
5. 이 경우 한 전구는 한 번만 끄거나 켤 수 있음
6. 단, 하나를 켰을 때, 좌우상하의 전구가 모두 켜지므로 이 경우 선택적으로 전구 스위치를 건드릴 지 말 지를 결정해야 함
7. 이러한 조건을 선정했을 때, (i+1,j) 전구를 넘어가면 (i,j) 전구는 다시는 건드릴 수 없음
8. 그렇다면, 맨 윗줄은 어떻게 정할지를 고려해야 함
9. 맨 윗 줄에 대해선 10개의 전구가 2가지 경우가 가능하므로 총 2**10인 2048개의 경우의수를 다 따져봐야 함
"""

import sys
inputs = sys.stdin.readline

def get_number_of_switchs_to_turn_off():
    table = []
    for _ in range(10):
        tmp = list(inputs().strip())
        for i in range(10):
            tmp[i] = True if tmp[i] =="O" else False # True/False : 불이 켜있음/ 불이 꺼있음
        table.append(tmp)

    
    ans = 101
    dirs = [(-1,0),(1,0),(0,0),(0,-1),(0,1)]
    for f in range(1<<10): # 1열을 누르는 경우의 수 
        tmp_table = []
        for i in range(10):
            tmp_table.append(table[i][:])

        cnt = 0
        # 1행 10칸 확인 (1 행에서 스위치를 누른 경우 모두 탐색)
        for i in range(10):
            if f & (1<<i): #i 번째 스위치를 누르거나 눌러있는 경우
                cnt += 1
                for dx,dy in dirs:
                    nx = 0 + dx
                    ny = i + dy #1열의 y는 0이므로
                    if 0 <= nx <= 9 and 0 <= ny <= 9:
                        tmp_table[nx][ny] = not tmp_table[nx][ny]
        
        # 1행은 끝났고, 2행부터는 위쪽의 전등이 켜있다면 눌러주는 식으로 진행
        for i in range(1,10):
            for j in range(10):
                if not tmp_table[i-1][j]:
                    continue
                for dx,dy in dirs:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx <= 9 and 0 <= ny <= 9:
                        tmp_table[nx][ny] = not tmp_table[nx][ny]
                cnt += 1

        #다 끝났는데 마지막 열에 켜 있는 경우 실패
        can = True
        for i in range(10):
            if tmp_table[-1][i]:
                can = False
        
        if can:
            ans = min(ans,cnt)
    print(ans)

if __name__=='__main__':
    get_number_of_switchs_to_turn_off()

