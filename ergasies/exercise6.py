import random
points_black=0
points_white=0
zigoi=[2,4,6,8]
monoi=[1,3,5,7]
#white=[]
#black=[]
chess=[]

# create board squares

for k in range(100):
    for i in range(1,9):
        for j in range(1,9):
            chess.append([i,j])

# define white squares
    #
    # for i in monoi:
    #     for j in zigoi:
    #         white.append([i,j])
    # for i in zigoi:
    #     for j in monoi:
    #         white.append([i,j])

    random.shuffle(chess)

    black_queen=[]
    black_queen.append(chess.pop())

    white_rook=[]
    white_rook.append(chess.pop())

    while black_queen==white_rook:
        white_rook.append(chess.pop())

    white_bishop=[]
    white_bishop.append(chess.pop())
    while black_queen==white_bishop or white_bishop==white_rook:
        white_bishop.append(chess.pop())

    # if black_queen==white_bishop:
    #     print("TrueQB")
    #
    # if black_queen==white_rook:
    #     print("TrueQR")
    #
    # if white_rook==white_bishop:
    #     print("TrueRB")

    # count points

    if black_queen[0][0]+black_queen[0][1]==white_rook[0][0]+white_rook[0][1]:
        points_black+=1
    elif black_queen[0][0]-black_queen[0][1]==white_rook[0][0]-white_rook[0][1]:
        points_black+=1
    elif black_queen[0][0]==white_rook[0][0]:
        points_black+=1
        points_white+=1
    elif black_queen[0][1]==white_rook[0][1]:
        points_black+=1
        points_white+=1
    elif black_queen[0][0]+black_queen[0][1]==white_bishop[0][0]+white_bishop[0][1]:
        points_black+=1
        points_white+=1
    elif black_queen[0][0]-black_queen[0][1]==white_bishop[0][0]-white_bishop[0][1]:
        points_black+=1
        points_white+=1

print("Points for black:",points_black)
print("Points for white:",points_white)

if points_black>points_white:
    print("Black is winner!")
elif points_black<points_white:
    print("White is winner!")
else:
    print("Equality for all :)")
