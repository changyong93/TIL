import sys
from collections import Counter, deque
from itertools import combinations
# input = sys.stdin.readline
input = iter([5,
"X S X X T",
"T X S X X",
"X X X X X",
"X T X X X",
"X X T X X",])

objects_set = set()
def check_escape(students=[], teachers=[], maps=[]):
    if len(objects_set)==0:
        # n = int(input().strip())
        # maps = [input().strip().split() for _ in range(n)]
        n = int(next(input))
        maps = [next(input).split() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if maps[i][j]=="T":
                    teachers.append((i,j))
                    continue
                if maps[i][j]=="S":
                    students.append((i,j))
                    continue
    
        for s_i,s_j in students:
            for t_i,t_j in teachers:
                if s_i == t_i:
                    s,e = min(s_j,t_j), max(s_j,t_j)
                    objects_set.update([(s_i, loc) for loc in range(s+1,e)])
                elif s_j==t_j:
                    s,e = min(s_i,t_i), max(s_i,t_i)
                    objects_set.update([(loc, s_j) for loc in range(s+1,e)])
        check_escape(students, teachers, maps)

    else:
        object_comb = list(combinations(objects_set,3))
        for objects in objects_set:
            for s_i,s_j in students:
                for t_i,t_j in teachers:
                    if s_i == t_i:
                        s,e = min(s_j,t_j), max(s_j,t_j)
                        tmp = [(s_i, loc) for loc in range(s+1,e)]

                    elif s_j==t_j:
                        s,e = min(s_i,t_i), max(s_i,t_i)
                        tmp = [(loc, s_j) for loc in range(s+1,e)]

                    if len(set.intersection(set(objects), set(tmp))) != 0:
                        
                        print("NO")
                        return
                    continue
        print("YES")

    

if __name__=="__main__":
    check_escape()