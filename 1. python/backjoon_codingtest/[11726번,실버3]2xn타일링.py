#파이썬의 재귀함수 호출범위는 1000번까지 가능하므로 해당 문제에서는 범위 제한을 풀지 않는다.
# sys.setrecursionlimit(limit_number)
# 해당 알고리즘 문제는 DP문제이다.
# n=1과 2일때 각각 1번과 2번 가지 케이스가 존재하고, n=3일때부터 n-1번째 케이스 개수와 n-2번째 케이스개수의 합계가 n번째 케이스 개수가 된다.


def dp(n):
    #n = 1,2일 경우엔 해당 값이 타일링 케이스 개수이므로 바로 반환
    if n in [1,2]:
        print(n)
        return

    #n = 3이상인 경우 dp 적용
    dp = [0,1,2]
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2])
    
    #결과 출력, 출력시 2xn 타일링 경우의수의 %10007 나머지만 반환
    print(dp[-1]%10007)

n = int(input())
dp(n)
