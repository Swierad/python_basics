import random

player =input("podaj 6 unikalnych liczb z zakresu od 1 do 49 oddzialająć liczby spacją\n")
player_list =player.split()


if len(player_list) == len(set(player_list)):                               
    pass
else:
    print("wprowadzono nieprawidłowe dane (liczby powtarzają się)")

if len(player_list) == 6:
    pass
else:
    print("wprowadzono nieprawidłowe dane (nieprawidłowa ilość liczb)")

random_list = []
i = 0
while i < 6:
    random_list.append(str(random.randint(1,50)))
    i += 1

final_list = []

for i in range(6):
    if player_list[i] in random_list:
        final_list.append(player_list[i])
    else:
        pass

if len(final_list) == 3:
    print ("gratulacje trafiłeś 3 oto szczęśliwe liczby:")
    print(final_list)
elif len(final_list) == 4:
    print ("gratulacje trafiłeś 4 oto szczęśliwe liczby:")
    print(final_list)
elif len(final_list) == 5:
    print ("gratulacje trafiłeś 5 oto szczęśliwe liczby:")
    print(final_list)
elif len(final_list) == 6:
    print ("gratulacje trafiłeś 6!!! oto szczęśliwe liczby:")
    print(final_list)
else:
    print("spróbój szczęścia ponownie")

