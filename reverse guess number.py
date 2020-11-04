print('pomyśl liczbę od 0 do 1000 a ja ją zgadnę w maksymalnie 10 próbach')
input('jeśli jesteś gotowy wwciśnij ENTER\n')
min = 0
max = 1000

result = False
try_number = 0

if try_number == 10:
    print('przegrałem')

while result == False:
    guess = (max-min)/2 + min
    guess = int(guess)
    print('Zgaduje ' + str(guess))
    feedback = input('wpisz 1. za dużo, 2. za mało 3. zgadłeś\n')
    if feedback == "zgadłeś":
        print('a nie mówiłem, odgadłem Twoją liczbę w {} ruchach'.format(try_number))
        result = True
    elif feedback == "za dużo":
        max = guess
        try_number +=1
    elif feedback == "za mało":
        min = guess
        try_number += 1
    else:
        print('nie oszukuj')
