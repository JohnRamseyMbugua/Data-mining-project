import time
time.sleep(.5)
print('Welcome')
time.sleep(.5)
print('This program extracts the individual letters from your name')
time.sleep(.5)
print('The code then counts the number of each vowel in your name')
time.sleep(.5)
a=('a')
e=('e')
i=('i')
o=('o')
u=('u')
time.sleep(.5)

while True:
    x = input("Please Enter your Name ")
    time.sleep(.9)
    for letter in (x):
        print(f' {letter}')
        time.sleep(.9)

    print('That spells', x)
    time.sleep(.9)

    count=x.count(a)
    print("The number of a is",count)
    time.sleep(.9)
    count=x.count(e)
    print("The number of e is",count)
    time.sleep(.9)
    count=x.count(i)
    print("The number of i is",count)
    time.sleep(.9)
    count=x.count(o)
    print("The number of o is",count)
    time.sleep(.9)
    count=x.count(u)
    print("The number of u is",count)
    time.sleep(.9)
    print("Please play again")
    time.sleep(.9)

    continue
