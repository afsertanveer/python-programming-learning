secret_number = 9
i=0
while i<3:
    guessed = int(input('Guess:'))
    if guessed==secret_number:
        print('You won')
        break
    else:
        i+=1

if i==3 :
    print('You Failed');
