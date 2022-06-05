import random

number = random.randint(1, 50)

print(number)
counter = 0
while True:
    counter += 1
    try:
        check = int(input("Please enter a number:\n"))
    except ValueError:
        print('Please give a number')
        continue
    if number == check:
        print('You won, congratulations!')
        break
    elif number < check:
        print('less')
        continue
    else:
        print('more')
        continue
print(f'You guested {counter} times.')
