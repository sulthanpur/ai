 # Tuple to store winning positions.
win_positions = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
 
def game(player):
    # diplay current mesh

    

    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print("", " | ".join(mesh[3:6]))
    print("---+---+---")
    print("", " | ".join(mesh[6:]))
 
    # Loop until player valid input cell number.
    while True:
        ch = input(f"Enter player {player}'s choice : ")
        if(ch not in pos) :
            print("Invalid position number.")
        else :
            mesh[int(ch)-1] = player
            pos.remove(ch)
            break
 
    # Return winning positions if player wins, else None.
    for wp in win_positions:
        count = 0
        for i in wp:
            if(mesh[i] == player):
                count+=1
        if(count==3):
            return True     
    return False

player1 = "X"
player2 = "O"
player = player1
mesh = list("123456789")
pos = list("123456789")

print("mesh : ",mesh)
 
for i in range(9):
	won = game(player)
	if won:
		print("\n", " | ".join(mesh[:3]))
		print("---+---+---")
		print("", " | ".join(mesh[3:6]))
		print("---+---+---")
		print("", " | ".join(mesh[6:]))
		print(f"*** Player {player} won! ***")
		break
	player = player1 if player == player2 else player2
else:
    # 9 moves without a win is a draw.
    print("Game ends in a draw.")


###  OUTPUT   ###

# Sample Output:
# 1 | 2 | 3
# ---+---+---
# 4 | 5 | 6
# ---+---+---
# 7 | 8 | 9
# Enter player X's choice : 5

# 1 | 2 | 3
# ---+---+---
# 4 | X | 6
# ---+---+---
# 7 | 8 | 9
# Enter player O's choice : 3

# 1 | 2 | O
# ---+---+---
# 4 | X | 6
# ---+---+---
# 7 | 8 | 9
# Enter player X's choice : 1

# X | 2 | O
# ---+---+---
# 4 | X | 6
# ---+---+---
# 7 | 8 | 9
# Enter player O's choice : 6

# X | 2 | O
# ---+---+---
# 4 | X | O
# ---+---+---
# 7 | 8 | 9
# Enter player X's choice : 9

# X | 2 | O
# ---+---+---
# 4 | X | O
# ---+---+---
# 7 | 8 | X
# *** Player X won! ***
