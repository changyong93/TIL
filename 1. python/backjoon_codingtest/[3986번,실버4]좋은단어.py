import sys
input = sys.stdin.readline

def count_good_words(n):
    res=0
    for i in range(n):
        check_word=input().strip()
        check=[]
        for s in check_word:
            if not check: # Check할 글자가 없는 경우 append
                check.append(s)
                continue

            if check[-1] == s: 
                check.pop() # Check list의 마지막 단어와 현재 글자가 같은 경우 둘 다 제거
            else:
                check.append(s) # Check list의 마지막 단어와 현재 글자가 다른 경우 추가
        res += 1 if not check else 0 #모든 단어가 쌍을 지어서 제거된 경우 좋은 단어라고 판단!
    print(res)

if __name__ == "__main__":
    n = int(input())
    count_good_words(n)