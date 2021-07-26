from collections import deque
import sys

def bell_check_and_take():
  global turn_count
  # 도도 벨
  if (do_ground and do_ground[0] == 5) or (su_ground and su_ground[0] == 5):
    #print("도도벨")

    #su_ground->do_deque
    while su_ground:
      do_deque.append(su_ground.pop())
    #do_ground->do_deque
    while do_ground:
      do_deque.append(do_ground.pop())
    
    #turn_count+=1

    #print("do,su 그라운드",do_ground,su_ground)
    #print("do,su덱",do_deque,su_deque)
  
  # 수연 벨
  elif do_ground and su_ground and do_ground[0] + su_ground[0] == 5:
    #print("수연벨")

    #do_ground->su_deque
    while do_ground:
      su_deque.append(do_ground.pop())
    #su_ground->su_deque
    while su_ground:
      su_deque.append(su_ground.pop())
    
    #turn_count+=1
  
    #print("do,su 그라운드",do_ground,su_ground)
    #print("do,su덱",do_deque,su_deque)
  

do_deque = deque()
su_deque = deque()
do_ground = deque()
su_ground = deque()

N,M = map(int,input().split())
for _ in range(N): #맨 아래에 적혀있는 수부터
  num1, num2 = map(int,input().split())
  do_deque.appendleft(num1)
  su_deque.appendleft(num2)

#print("do덱",do_deque)
#print("su덱",su_deque)

i = 0 #번갈아가면서 내는 순서 정하기
#turn_count = 0 #게임진행횟수
while i != M:
  if i%2==0:
    do_ground.appendleft(do_deque.popleft())
  else:
    su_ground.appendleft(su_deque.popleft())
  
  if not do_deque:
    print("su")
    sys.exit(0)
  
  if not su_deque:
    print("do")
    sys.exit(0)
  
  #turn_count +=1
  #print("do,su 그라운드",do_ground,su_ground)
  #print("do,su덱",do_deque,su_deque)

  bell_check_and_take()
  
  i+=1



if len(do_deque) == len(su_deque):
  print("dosu")
elif len(do_deque) > len(su_deque):
  print("do")
else:
  print("su")
