import sys
inputs = sys.stdin.readline
if __name__=="__main__":
    # 전체 팀 수, 카약이 부서진 팀 수, 여분 카약을 가진 팀 수
    N,M,K = map(int,inputs().strip().split(" "))
    teams = [0]*(N+2)

    # 카약이 부서진 팀은 -1
    for broken in map(int,inputs().strip().split(" ")):
        teams[broken] -= 1

    # 여분의 카약이 있는 팀 +1
    for spare in map(int,inputs().strip().split(" ")):
        teams[spare] += 1
    
    for i in range(len(teams)):
        if teams[i] == -1: #카약이 부서진 팀의 경우
            if teams[i-1] == 1: #왼쪽 팀에 여분의 카약이 있는 경우
                teams[i-1] = 0
                teams[i] = 0
            elif teams[i+1] == 1: #오른쪽 팀에 여분의 카약이 있는 경우
                teams[i+1] = 0
                teams[i] = 0
            
    print(teams.count(-1))
