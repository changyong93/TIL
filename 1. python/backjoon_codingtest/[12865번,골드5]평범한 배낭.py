# DP 문제
# n,v = map(int,"4 7".split())
# inputs = iter(["6 13","4 8",'3 6','5 12'])
# stuff = [list(map(int,next(inputs).split())) for _ in range(n)]

# 물품 개수와, 최대 무게
n, v = map(int,input().split())

# 물건 및 물건 가치
stuff = [list(map(int,input().split())) for _ in range(n)]

# dp로 풀기 위해 2d matrix 생성
# 현재 값 기준, 이전 index의 값을 호출해야 하므로, 0으로 된 행과 열을 추가
knapsack = [[0]*(v+1) for _ in range(n+1)]


for i in range(1,n+1):
    weight,value = stuff[i-1]
    for j in range(1,v+1):
        #현재 물건의 무게가 최대 무게보다 큰 경우, 동일 열, 이전 행의 값을 가져온다.
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        # 물건의 무게가 최대 무게를 넘을 경우, 1)현재 넣을 물건과 남은 무게로 같이 넣을 수 있는 물건 2) 이전 행 idx의 물건 무게 중 더 큰 값을 가져온다.
        else:
            knapsack[i][j] = max(knapsack[i-1][j], stuff[i-1][1] + knapsack[i-1][j-stuff[i-1][0]])

#항상 마지막 행 & 마지막 열의 값이 최대값
print(knapsack[-1][-1])
