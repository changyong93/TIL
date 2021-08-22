# DP를 이용한 문제

ipnut = int(input())
numbers = list(map(int, input().split()))

#dp list의 첫 값은 무조건 첫번째 입력값이므로 바로 저장
dp = [numbers[0]]

for i in range(1,len(numbers)):
    # 현재 더할 값과, 이전까지 누적값+현재 값 중 큰 값을 dp list에 append 한다
    dp.append(max(numbers[i], numbers[i]+dp[i-1]))
print(max(dp))
