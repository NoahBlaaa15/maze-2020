number = int(input('pls give number: '))
Status = 0
while Status == 0:
    print('a')
    print('b')
    print('c')

    if number == 0:
        print('Number is 0')

    print('d')

    if number == 1:
        print('Number is 1. Ending loop')
        Status = 1
        continue

print('Loop has ended')