def fub(*args1):
    print(type(args1)) #args is a tuple class
    if(len(args1) == 2):
        print('My name is',args1[0],args1[1]) # comma ',' works like space
    else:
        print('My name is',args1[0])


fub('shahrukh', 'khan')
fub('shahrukh')
