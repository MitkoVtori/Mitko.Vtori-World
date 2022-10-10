from random import randint
from time import sleep

targets = [randint(1, 500) for length in range(randint(6, 21))]
print('''############################################################################################################################################
#           Welcome to the Moving Target game!                                                                                             #
#                                                                                                                                          #
#           The rules are simple:                                                                                                          #
#           You'll receive a random list of targets,                                                                                       #
#           every target has it's own number(integer).                                                                                     #
#                                                                                                                                          #
#           There are three options:                                                                                                       #
#           Shoot {Target} {Power}: Shooting the target's number with the chosen power.                                                    #
#           Example: Shoot 1 200                                                                                                           #
#           If 200 is smaller or equal to the first's target number, your target will be reduced by the power.                             #
#           If 200 is bigger than your target with 5 or more, the power is too much and you'll miss the shot.                              #
#           If the target's value it's between -5 and 0, the target will be removed.                                                       #
#           Sometimes, while you're playing there's a chance for the game to add a target.                                                 #
#           Second option, Strike {Target} {Radius}: You'll directly remove the target, and all the targets in the chosen radius.          #
#           Example: Strike 4 2                                                                                                            #
#           Removes the 2nd, 3rd, 4th, 5th and 6th target, because 4th target is your chosen target, and 2 is your chosen radius.          #
#                                                                                                                                          #
#                               BE CAREFUL! At some point the game will decide to say End and the game ends!                               # 
#                                      The game is considered won if there aren't any targets                                              #
#                            At the end of the game will be printed a list of the left targets value                                       #
#                                           You can also End the game by typing End                                                        #
#                                                                                                                                          #
#                                     Made by - Dimitar Dimitrov  |  Mitko.Vtori                                                           #
#                                                                                                                                          #
#                                                                                                                                          #
############################################################################################################################################''')
print()
print()
sleep(0.2)
input("Type anything to start: ")
print("..........")
sleep(0.3)
print("..............")
sleep(0.5)
print("....................")
sleep(0.3)
print("targets have been set!")
sleep(0.5)
print("###############################")


def list_targets():
    for number_targets in range(len(targets)):
        if number_targets % 3 == 0:
            print('#')
            print('#')
        print("#  ⌖🎯⌖", end='  ')


list_targets()
print()
end = randint(10, 45)
end_counter = 0
add = randint(5, 15)
add_counter = 0
try:
    while True:
        end_counter += 1
        add_counter += 1
        sleep(0.3)
        command = input("Choose between Shoot and Strike: ")
        if command.lower() == 'end' or end_counter == end:
            break
        elif add_counter == add:
            targets.insert(randint(1, len(targets) - 1), randint(1, 300))
            print("Adding new target...")
            sleep(0.5)
            print(".............")
            sleep(0.3)
            list_targets()
        indexes = command.split(' ')
        try:
            index = int(indexes[1]) + 1
            power = int(indexes[2])
            value = int(indexes[2])
            radius = int(indexes[2]) + 1
        except IndexError:
            print("Invalid input. Try again!")
            continue
        except ValueError:
            print("Invalid input. Try again!")
            continue
        except TypeError:
            print("Invalid input. Try again!")
            continue
        if indexes[0].lower() == "shoot":
            if index - 1 >= len(targets) or index < 0:
                print("Index out of range")
                continue
            if targets[index] - power < -5:
                print("The power was too much and you missed!")
                continue
            targets[index] -= power
            if targets[index] <= 0:
                print("Your shot was great!")
                targets.pop(index)
                list_targets()
            else:
                print(f'- {power} power!')
        elif indexes[0].lower() == "strike":
            if index - 1 >= len(targets) or (index - 1) + (radius - 1) >= len(targets) or index - radius < 0:
                print("Strike missed!")
                continue
            try:
                for indices in range(radius):
                    targets.pop(index - 1)
                    targets.pop(index)
                targets.pop(index - radius)
                list_targets()
            except IndexError:
                print("Index out of range")
                continue
except IndexError:
    print()

if len(targets) <= 0:
    print("Congrats! You win! :)")
else:
    print("Sorry, you lose :(")
print(*targets, sep="|")
