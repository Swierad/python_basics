from random import randint

rnd_num = int(randint(1,101))
result = False


while result == False:
    try:
        answer = int(input("podaj liczbę\n"))
    except Exception:
        print("podana wartość to nie liczba")
        continue    # eliminuje przerwę w programie
    if answer > rnd_num:
        print("za dużo!")
    elif answer < rnd_num:
        print("za mało!")
    else:
        print("Brawo, to jest ta liczba")
        result = True




