import random

print("vytej ve hre, tvym ukolem je uhadnout cislo na 7 pokusu od: 1 do 100")

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input('zadej tvuj typ: '))

    if my_guess == number_to_guess:
        print(f'SPravne cislo bylo:{number_to_guess} a ty jsi ho nasel!! na {guess_counter} pokus')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'tentokrat to nevyslo spravne cislo bylo: {number_to_guess} hodne stesti pri dalsim pokusu')

    elif my_guess > number_to_guess:
        print('cislo je nizsi')

    elif my_guess < number_to_guess:
        print('cislo je vyssi')
