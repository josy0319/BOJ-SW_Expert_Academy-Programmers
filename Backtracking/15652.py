#BOJ - N과 M(4)

'''
backtracking
'''

import sys

input = sys.stdin.readline

def solve(L, w):
    if L==m+1:
        for i in range(1, m+1):
            print(res[i], end=' ')
        print()
    else:
        for i in range(w, n+1):
            res[L] = i
            solve(L+1, i)

n, m = map(int, input().split())
res = [0]*(m+1)
solve(1, 1)
