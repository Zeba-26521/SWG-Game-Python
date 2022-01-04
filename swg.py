import random
swg=('S','W','G')
ch=5
youcount=0
comcount=0
drawcount=0
while(ch>=1):
    you = input("Enter S or W or G: ")
    com = random.choice(swg)
    print(f"Computer choose:{com} and You Choose:{you}")
    s = set()
    s.add(com)
    s.add(you)
    win = ''
    if s == {'W', 'S'}:
        win = 'S'
    elif s == {'G', 'S'}:
        win = 'G'
    elif s == {'W', 'G'}:
        win = 'W'
    elif s == {'W'} or {'S'} or {'G'}:
        win = 'D'
    # First if end here:For win assighnment done

    if win == 'D':
        print('This match:Draw')
        drawcount+=1
    elif win == you:
        print('This match:You Won')
        youcount+=1
    else:
        print('This match:Computer Won')
        comcount += 1

    ch=ch-1

print(f"Total number of Matched you won: {youcount}")
print(f"Total number of Matched Computer won: {comcount}")
print(f"Total number of Matched Draw: {drawcount}")

if youcount==comcount:
    print('Series DRAW')
elif youcount > comcount:
    print('YOU won the Series ')
else:
    print('COMPUTER Won the Series')