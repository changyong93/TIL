import sys
import re
input = sys.stdin.readline

#224ms
# def check_string(): #re 패키지 사용
#     n = int(input())
#     test = input().strip()
#     for i in range(len(test)):
#         if test[i]=="*":
#             s,e = test[:i],test[i+1:]
#             break

#     reg = f"{s}.*{e}"
#     for i in range(n):
#         tmp = re.sub(reg,"",input().strip())
#         if tmp=="":
#             print("DA")
#         else:
#             print("NE")

#104ms
def check_string(): #re X
    n = int(input())
    case = input().strip()
    for i in range(len(case)):
        if case[i]=="*":
            left,right = case[:i], case[i+1:] #* 위치를 중심으로 좌우 확인할 string 저장
            break

    for i in range(n):
        test = input().strip()
        if len(test) < len(left+right): #확인할 string보닥 길이가 짧으면 NE
            print("NE")
            continue
        if test[:len(left)]!=left or test[-len(right):]!=right: #좌측 혹은 우측 string이 다르면 NE
            print("NE")
            continue
        print("DA") #나머진 DA

if __name__=="__main__":
    check_string()
