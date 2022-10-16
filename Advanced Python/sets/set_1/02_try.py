'''To avoid showing error to the User'''

while(True): #to keep in loop
    print('Press space bar to quit')
    a = input('Enter your Rank : ')
    if a == ' ':
        break
    try:  
        print('Trying...')
        a = int(a)
        if a<11:
            print('Congrats! You Have Qualified the Exam')
        else:
            print('Sorry! You could not qualify the exam')
    except Exception as e:
        print(f"Your input resulted in Error {e}")
print('Thank you')
