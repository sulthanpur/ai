b=['']*9
w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
p='X'
for l in range(9):
    print(f"{b[0]}|{b[1]}|{b[2]}\n{b[3]}|{b[4]}|{b[5]}\n{b[6]}|{b[7]}|{b[8]}")
    m=int(input(f"{p}'s move(0-8):"))
    if b[m]!='':
        print("Taken");continue
    b[m]=p
    if any(b[i]==b[j]==b[k]==p for i,j,k in w):
        print(f"User {p} WINs");break
    p='O' if p=='X' else 'X'
else:
    print("Draw")