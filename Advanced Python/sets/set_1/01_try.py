while(True): #to keep in loop
     print('Press Q to quit')
     a = input('Enter your Rank')
     if a == 'q' or a == 'Q':
         break
     a = int(a)

     if a<11:
         print('Congrats! You Have Qualified the Exam')
     else:
         print('You could not qualify the exam')

print('Thank you')
