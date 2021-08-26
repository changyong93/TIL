import sys

def hanoi(n,a,b,c): #a:시작점 b.중간지점, c:도착점
    if n==1:
        move.append(f"{a} {c}")
        return

    hanoi(n-1, a,c,b) #모든 원판을 C에 위치시키기 위해서 나머지를 B로 이동
    move.append(f"{a} {c}") #가장 밑에 있는 원판 한 장을 C로 이동
    hanoi(n-1, b,a,c)

if __name__=="__main__":
    n = int(input())
    move = []
    hanoi(n,1,2,3)

    k = len(move)
    print(k)
    for i in range(k):
        print(move[i])
