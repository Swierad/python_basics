from random import randint

def user_number(x):
    try:
        x = int(x)
    except ValueError:
        print("To nie jest liczba! "
              "Spróbuj ponownie.")


cpu_number = randint(1, 100)
number_of_tries = 1
check = False

while check == False:
    user_no = input("Hey, can You give me a number?\n")
    user_number(user_no)
    if int(user_no) < cpu_number:
        number_of_tries += 1
        print('za mało!')

    elif int(user_no) > cpu_number:
        number_of_tries += 1
        print('za dużo')
    else:
        number_of_tries += 1
        check = True
print("Zgadłeś za {} razem".format(number_of_tries))
