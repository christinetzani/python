import random

winMovesList=[]

for games in range(100):
    square=[
        [[1,2,3],[1,2,3],[1,2,3]],
        [[1,2,3],[1,2,3],[1,2,3]],
        [[1,2,3],[1,2,3],[1,2,3]],
    ]

    newList=[]

    print(square[1])
    print(square[1][1])
    print(square[2][0][2])


    print("\n start \n")
    winMoves=0
    for i in range(50):
        winMoves+=1

        print(i)
        play=[random.randint(0,2),random.randint(0,2),random.randint(0,2)]
        while type(square[play[0]][play[1]][play[2]])==str:
            play=[random.randint(0,2),random.randint(0,2),random.randint(0,2)]

        square[play[0]][play[1]][play[2]]=str(square[play[0]][play[1]][play[2]])

        print("\n")
        count=0
        if type(square[0][0][0])==str and type(square[1][1][1])==str and type(square[2][2][2])==str: #1,2,3 Primary diagonial
            count=3
        if type(square[0][0][2])==str and type(square[1][1][1])==str and type(square[2][2][0])==str: #3,2,1 Primary diagonial
            count=3
        if type(square[2][0][0])==str and type(square[1][1][1])==str and type(square[0][2][2])==str: #1,2,3 Secondary diagonial
            count=3
        if type(square[2][0][2])==str and type(square[1][1][1])==str and type(square[0][2][0])==str: #3,2,1 Secondary diagonial
            count=3
        if count==3:
             break
        for k in range(3):
            if type(square[0][0][k])==str and type(square[1][1][k])==str and type(square[2][2][k])==str: #1,1,1 | 2,2,2 | 3,3,3 Primary diagonial
                count=3
            if type(square[2][0][k])==str and type(square[1][1][k])==str and type(square[0][2][k])==str: #1,2,3 Secondary diagonial
                count=3
            if type(square[k][0][0])==str and type(square[k][1][1])==str and type(square[k][2][2])==str: #1,2,3 horizontal
                count=3
            if type(square[2-k][0][2])==str and type(square[2-k][1][1])==str and type(square[2-k][2][0])==str: #3,2,1 horizontal
                count=3
            if type(square[0][k][0])==str and type(square[1][k][1])==str and type(square[2][k][2])==str: #1,2,3 vertical 1,2,3
                count=3
            if type(square[0][k][2])==str and type(square[1][k][1])==str and type(square[2][k][0])==str: #3,2,1 vertical
                count=3

            if count ==3:
                break
            for j in range(3):
                if type(square[k][0][j])==str and type(square[k][1][j])==str and type(square[k][2][j])==str: #1,1,1 horizontal
                    count=3
                if type(square[0][k][j])==str and type(square[1][k][j])==str and type(square[2][k][j])==str: #1,1,1 vertical
                    count=3
                    if count ==3:
                        break
                        print(i, "done")
            if count ==3:
                break
        if count == 3:
             break
        # print(square[m])
    winMovesList.append(winMoves)
print(winMovesList)

sum=0
for j in range(len(winMovesList)):
    sum+=winMovesList[j]

print(sum/len(winMovesList))
