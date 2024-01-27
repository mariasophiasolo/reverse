# ask user to input their year of birth then reverse it

def reverse_digits(year):
    # convert the user input to a string and reverse it
    print("Year of Birth:", year)
    reverse_digits = ' '.join(str(year)[::-1])

    # print now the reversed digit with spaces in between
    print("Reverse digits: ", reverse_digits)

user_input = int(input("Enter your year of birth: "))
reverse_digits(user_input)

