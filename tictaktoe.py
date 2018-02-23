a = [' ',' ',' ']
b = [' ',' ',' ']
c = [' ',' ',' ']
count = 0
ch = 'X'
cha = 'O'
n = 1

def action():
    global count
    global n
    x = int(input())
    import os
    os.system("cls")
    if x>9:
        print("Please enter the value between 1-9")
        n-=1
        count-=1
    if count % 2 == 0 and count <= 9:
        count+=1
        if x<=3:
            if (a[x-1]=='X') or (a[x-1] == 'O'):
                print("Wrong Move")
                n-=1
                count-=1
            else:
                a[x-1]=ch
        elif (x >= 4)and (x <= 6):
            if (b[x-4]=='X') or (b[x-4] == 'O'):
                print("Wrong Move")
                n-=1
                count-=1
            else:
                b[x-4]=ch
        elif (x >= 7) and (x<=9):
            if (c[x-7]=='X') or (c[x-7] =='O'):
                print("Wrong Move")
                n-=1
                count-=1
            else:
                c[x-7]=ch
        for x in a:
            print(x, end=" |")
        print("\n__________")
        for x in b:
            print(x, end=" |")
        print("\n__________")
        for x in c:
            print(x, end=" |")
        print("\n__________")
    elif count<=9:
        count+=1
        if x <= 3:
            if (a[x - 1] == 'X') or (a[x - 1] == 'O'):
                print("Wrong Move")
                n-=1
                count-=1
            else:
                a[x-1]=cha
        elif (x>=4) and (x<=6):
            if (b[x - 4] == 'X') or (b[x - 4] == 'O'):
                print("Wrong Move")
                n -= 1
                count-=1
            else:
                b[x-4]=cha
        elif (x >= 7) and (x <= 9):
            if (c[x - 7] == 'X') or (c[x - 7] == 'O'):
                print("Wrong Move")
                n -= 1
                count-=1
            else:
                c[x-7]=cha
        for x in a:
            print(x, end=" |")
        print("\n__________")
        for x in b:
            print(x, end=" |")
        print("\n__________")
        for x in c:
            print(x, end=" |")
        print("\n__________")
while n <= 9:
    action()
    if(((a[0]==a[1]==a[2]=='X') or (b[0]==b[1]==b[2]=='X') or (c[0]==c[1]==c[2]=='X'))or ((a[0]==b[0]==c[0]=='X') or (a[1]==b[1]==c[1]=='X') or (a[2]==b[2]==c[2]=='X')) or ((a[0]==b[1]==c[2]=='X') or (a[2]==b[1]==c[0]=='X'))):
        print("Player 1 wins")
        break
    elif(((a[0]==a[1]==a[2]=='O') or (b[0]==b[1]==b[2]=='O') or (c[0]==c[1]==c[2]=='O'))or ((a[0]==b[0]==c[0]=='O') or (a[1]==b[1]==c[1]=='O') or (a[2]==b[2]==c[2]=='O')) or ((a[0]==b[1]==c[2]=='O') or (a[2]==b[1]==c[0]=='O'))):
        print("Player 2 wins")
        break
    
    n += 1
