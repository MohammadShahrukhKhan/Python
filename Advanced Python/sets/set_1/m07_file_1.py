from pip import main


def greet(name):
    print(f'Good Morning, {name}')

print(__name__)    

if __name__ == "__main__": #prevents to run further program in the main file
    o = input('Enter your Name')
    greet(o) 
      