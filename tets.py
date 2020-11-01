def user_number():
    user_no = input("Hey, can You give me a number?\n")
    try:
        if user_no == int(user_no):
            return user_no
    except ValueError:
        print("To nie jest liczba! "
              "Spróbuj ponownie.")
        user_number()
    return user_no