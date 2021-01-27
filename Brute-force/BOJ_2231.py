N = int(input())
ans=0 #생성자가 없을 시 답은 0

for num in range(N):
  #리스트 컴프리헨션으로 각 자릿수의 합 구하는 법
  now_num = num + sum([int(i) for i in str(num)])
  if now_num == N: #생성자가 존재할 때
    ans=num
    break

print(ans)
