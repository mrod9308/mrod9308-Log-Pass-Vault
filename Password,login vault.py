o_start = input('To Start Press Enter: ')
login_info = input('What is your login : ')
password_info = input('What is your password : ')
confirm = input('Is this correct please type Y for Yes ? ')


def confirm_1():  #Confirms Value Y & outputs to user to confirm answer.
    if confirm == str('Y'):
        print('Your Password & Login have been Securely stored !')
    elif confirm != 'Y':
        print('Try again, not Confirmed!!')
        print(0, 1, 2, 3, '.... out')
        greet = 'Welcome to login Vault!'
        print(greet)
        print('Password: ', password_info)
        print('login: ', login_info)


confirm_1()
print('Program Done')
