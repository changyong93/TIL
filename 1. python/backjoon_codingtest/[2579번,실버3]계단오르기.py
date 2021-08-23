import sys
input = sys.stdin.readline

def solve(n):
    dp = [0 for _ in range(n+3)]
    stairs = [0 for _ in range(n+3)]
    
    for i in range(1,n+1):
        stairs[i] = int(input())

    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    
    #마지막 n층은 반드시 밟아야 하므로, 아래 두 가지 경우가 가능
    #마지막층(n) + 이전 층 점수(n-1) + 세층 전 최대점수(n-3) // 마지막층(n) + 두층 전 최대점수(n-2) 
    for i in range(4,n+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    
    #마지막 층의 점수 반환
    print(dp[n])


if __name__ == "__main__":
    n = int(input())
    solve(n)
