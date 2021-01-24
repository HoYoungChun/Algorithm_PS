#가능한 경우 리스트에 넣어두고 for문으로 접근하기
going = [(+2,-1),(+2,+1),(-2,-1),(-2,+1), \
(+1,-2),(+1,+2),(-1,-2),(-1,+2)]

my_str = input()

#ord는 문자를 아스키코드로
#chr는 아스키코드를 문자로
x=ord(my_str[0])-ord('a')+1
y=int(my_str[1])

ans = 0

for go in going:
  if (1<=x+go[0]<=8) and (1<=y+go[1]<=8):
    ans+=1

print(ans)
