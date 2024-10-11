# import random

# my_number = 13
# rand_number = random.randint(1,50)

# while my_number !=rand_number:
#     print(f"I guessed {rand_number}")
#     rand_number = random.randint(1,50)

# print(f"Well done me! I guessed {rand_number} and that matched your number {my_number}!")

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')