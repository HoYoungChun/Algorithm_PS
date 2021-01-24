n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x+dx[i]
      ny = y+dy[i]
      if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
      x,y=nx,ny

print(x,y)

#내가 처음에 푼 풀이
# N = int(input())
# plans = input().split()

# now_x = 1
# now_y = 1

# for plan in plans:
#   if plan=='R':
#     if now_y+1 <= N:
#       now_y +=1
#   elif plan=='L':
#     if now_y-1 >= 1:
#       now_y -=1
#   elif plan=='D':
#     if now_x+1 <= N:
#       now_x +=1
#   elif plan=='U':
#     if now_x-1 >= 1:
#       now_x -=1

# print(now_x, now_y)
