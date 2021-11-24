import sys
inputs = sys.stdin.readline

if __name__=="__main__":
    N = int(inputs().strip())
    
    for _ in range(N):
        cnt = 0
        num = int(inputs().strip())
        #Test Case가 1일 경우 한 자리수를 출력 => 1    
        if num == 1:
            print(1)
            continue
        
        #Test Case가 2이상인 경우
        for i in range(9,1,-1):
            while num%i==0:
                num /= i
                cnt += 1
        
        #2~9의 숫자를 반복적으로 사용하여 나눴을 때 1로 변하지 않을 경우 -1
        print(cnt if num == 1 else -1)
