import itertools

N,M = map(int,input().split())
cards = list(map(int,input().split()))
cards = list(itertools.combinations(cards,3)) #nC3 조합

summ=-1
for card in cards:
  if summ<sum(card) and sum(card)<=M:
    summ=sum(card)

print(summ)
