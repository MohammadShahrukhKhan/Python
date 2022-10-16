# Building a simple Login and SignUp System.

print('Create Your Account Now')

Username1 = input("Enter User Name: ")
Password1 = input('Enter Password: ')

print('Your Account has been created Successfully!!')
print('Login Now')

Username2 = input("Enter User Name: ")
Password2 = input('Enter Password: ')

if Username1 == Username2 and Password1 == Password2:
    print('Logged in Successfully !')
else:
    print("Invalid credentials")