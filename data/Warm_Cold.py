import random

number = random.randint(1, 50)
value = input("Please enter a number:\n")
counter = 0
while True:
    counter += 1
    if number == int(value):
        print('you won')
        break
    elif number < int(value):
        print('less')
        value = input("Please enter a number:\n")
    else:
        print('more')
        value = input("Please enter a number:\n")
print(f'you guested {counter} times')
