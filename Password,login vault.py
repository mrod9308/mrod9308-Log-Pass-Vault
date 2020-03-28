def confirm_1():
    if confirm == str('Y'):
        print('Your Password & Login have been Securely stored !')
    elif confirm != 'Y':
        print('Try again, not Confirmed!!')

    while True:
        print(0, 1, 2, '...' + ' Process is Completed')
        break


greet = 'Welcome to login Authenticator!'
to_start = input('To Start Press Enter: ')

login_info = input('What is your login : ')
password_info = input('What is your password : ')

print('Password: ', password_info)
print('login: ', login_info)
confirm = input('Is this correct please type Y for Yes ? ')

confirm_1()
