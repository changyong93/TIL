import sys

k, n = map(int, sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for _ in range(k)]

# k,n = map(int,"4 11".split())
# lans = list(map(int,["802","743","457","539"]))

s, e = 1, max(lans)
while s <= e:
    # print(s, e)
    mid = (s + e) // 2
    cnt = sum(line // mid for line in lans)
    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1
    # print(s, e, mid, cnt)
print(e)
