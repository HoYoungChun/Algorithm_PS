from collections import deque
deq = deque()

N = int(input())
skills = list(map(int,input().split()))
skills.reverse()

for i,skill in enumerate(skills):
  if skill == 1:
    deq.appendleft(i+1)
  elif skill == 3:
    deq.append(i+1)
  elif skill == 2:
    tmp = deq.popleft()
    deq.appendleft(i+1)
    deq.appendleft(tmp)

print(*list(deq))

