def confirm_1():  # Confirms Value Y & outputs to user to confirm answer.
    greet = 'Welcome to login Vault!'
    print(greet)
    to_start = input('To Start Press Enter: ')
    login_info = input('What is your login : ')
    password_info = input('What is your password : ')
    confirm = input('Is this correct please type Y for Yes ? ')
    if confirm == str('Y'):
        print('Your Password & Login have been Securely stored !')
    elif confirm != 'Y':
        print('Try again, not Confirmed!!')
        print(0, 1, 2, 3, '.... out')
        print('Password: ', password_info)
        print('login: ', login_info)


confirm_1()
print(input('Program Done, Press Enter to Exit'))
