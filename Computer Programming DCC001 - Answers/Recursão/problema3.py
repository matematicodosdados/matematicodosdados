def mdc(x,y):
    if y == 0:
        return x 
    else:
        return mdc(y,x%y)
x = int(input('Digite x: '))
x = int(input('Digite y: '))
print(mdc(x,y))