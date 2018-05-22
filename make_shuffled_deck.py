import random
import sys

def print_deck(deck):
	for i in deck:
		print(i["key"],i["number"])

deck=[]
n=int(sys.argv[1])
print(n)
cards=[]
for i in range(0,52):
	cards.append(0)

suite=['spade','diamond','hearts','clubs']
card=['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
count=0
print(n*52)
while(count < (n*52) ):
	k=random.randint(0,3)
	number=random.randint(0,12)
	if(cards[(k * 13)+number]<n):
		cards[(k*13)+number]+=1
		count+=1
		deck.append({"key" : suite[k],"number": card[number]})
print_deck(deck)
