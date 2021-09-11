import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    max_idx = -1 #숫자가 가장 높은 사람의 번호
    max_num = 0 #가장 높은 높읜 사람의 카드 합 첫 째 자리 번호
    for i in range(n): #n명에 대해 각각 확인
        q = deque()
        # cards = deque(map(int, input().strip().split()))
        cards = deque(map(int, next(inputs).strip().split()))
        for _ in range(len(cards)):
            card = cards.popleft()
            q.append((card, cards.copy(), 1))
            cards.append(card)

        while q:
            num, cards, k = q.popleft()            
            if k == 3:
                if max_num < num: #번호가 더 큰 경우
                    max_num = num #번호 지정
                    max_idx = i #사람 변경
                elif max_num == num: #번호가 같을 경우
                    if max_idx < i: #사람 번호가 더 큰 경우만 변경
                        max_idx = i
                else:
                    continue #k=3인경우 더 이상 탐색할 필요가 없으므로 continue로 다시 while문의 첫번째 코드부터 실행

            for _ in range(len(cards)):
                candi = cards.popleft()
                nxt_num = (num+candi)%10
                q.append((nxt_num, cards.copy(), k+1))
                cards.append(candi)
    print(max_idx+1)

inputs = iter(['3', '7 5 5 4 9', '1 1 1 1 1', '2 3 3 2 10'])

if __name__=="__main__":
    # n = int(input().strip())
    n = int(next(inputs).strip())
    bfs(n)
