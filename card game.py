# fortwse vivlio8hkh gia anakatoma
import random

figures=["J","Q","K"]
numbers=list(range(1,11))
axia=numbers+figures
symbols=["D","H","C","S"]
# etoimase thn trapoula
cards=[]
for i in symbols:
    for j in axia:
        # pros8ese ena ena ta xartia
        # gia ka8e symbolo
        cards.append([i,j])
# anakatwse ta xartia
random.shuffle(cards)
# moirase xartia ston player1
player1=[]
player1.append(cards.pop())
player1.append(cards.pop())

# moirase xartia ston player2
player2=[]
player2.append(cards.pop())
player2.append(cards.pop())

# ektupwse ta xartia tou ka8e paixth
print ("Player1:",player1)
print ("Player2:",player2)

# ypologise to score tou p1
s1=0
for i in player1:
    # an figoura pros8ese 10
    if i[1] in figures:
        s1=s1+10
    # an oxi thn aksia tou xartiou
    else:
        s1=s1+i[1]
print("Score player1",s1)

# ypologise to score tou p2
s2=0
for i in player2:
    # an figoura pros8ese 10
    if i[1] in figures:
        s2=s2+10
    # an oxi thn aksia tou xartiou
    else:
        s2=s2+i[1]
print("Score player2",s2)

# des poios kerdise
if s1>s2:
    print("P1 wins!")
elif s1<s2:
    print("P2 wins!")
else:
    print("Draw...")
