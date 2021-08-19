#연속하는 n일의 온도의 합이 가장 높은 구간을 선택하는 것이므로
#window를 지정해놓고 최대값을 반환하면 될 것이라 생각

n,k = map(int,input().split())
temperatures = list(map(int,input().split()))

max_tmp = sum(temperatures[:k])
tmp = max_tmp
for i in range(k,n):
    tmp += temperatures[i]-temperatures[i-k]
    if max_tmp < tmp:
        max_tmp = tmp
print(max_tmp)