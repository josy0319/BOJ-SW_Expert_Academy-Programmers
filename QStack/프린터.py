#programmers - 프린터

'''
stack
'''

from collections import deque
def solution(p, l):
    res=0
    temp=deque([0] * len(p))
    temp[l]=1
    while True:
        if len(p)==0 or len(p)==1:
            res+=1
            break
        if p[0]>=max(p[1:]):
            p.pop(0)
            count=temp.popleft()
            res+=1
            if count==1:
                break
        else:
            p.append(p.pop(0))
            count=temp.popleft()
            temp.append(count)
    return res

#이전 코드
def solution(priorities, location):
    answer = 0
    temp = [0] * len(priorities)
    temp[location] = 1
    total=0
    for i in range(0,len(priorities)):
        for k in range(0,len(priorities)):
            for j in range(1,len(priorities)):
                if priorities[0] < priorities[j] : 
                    a = priorities.pop(0)
                    priorities.append(a)
                    b = temp.pop(0)
                    temp.append(b)                    
                    break
        a=priorities.pop(0)
        b=temp.pop(0)
        total += 1
        if(b==1):
            answer = total
            break
    return answer
