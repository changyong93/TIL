import sys

def select_operator(ans, now):
    if now == n:
        calc(ans)
        return
    
    select_operator(ans+" "+str(now+1), now+1)
    select_operator(ans+"+"+str(now+1), now+1)
    select_operator(ans+"-"+str(now+1), now+1)
    

def calc(ans):
    tmp = ans.replace(" ","")
    if eval(tmp)==0:
        print(ans)
    

inputs = sys.stdin.readline
if __name__=="__main__":
    N = int(inputs())    
    n_list = [int(inputs().strip()) for _ in range(N)]
    for n in n_list:
        select_operator('1', 1)
        print()