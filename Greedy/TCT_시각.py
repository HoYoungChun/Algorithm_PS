N = int(input())
ans = 0

for i in range(N+1):
  for j in range(60):
    for k in range(60):
      t = str(i)+str(j)+str(k)
      if '3' in t:
        ans+=1

print(ans)
