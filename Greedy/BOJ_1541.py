exp = input().split('-') #'-'를 기준으로 수식분리

#'-'를 기준으로 분리된 수식 중 맨앞에 있는 수식만 양수
ans = sum(map(int,exp[0].split('+'))) 
for i in range(1,len(exp)):
  ans -= sum(map(int,exp[i].split('+'))) # 분리된 수식의 덧셈을 계산하여 빼준다

print(ans)
