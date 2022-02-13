# author: Joshua Wells
# date: 2/13/2022
import math


def is_prime(prime_candidate):
    if prime_candidate < 2:
        return False

    for num in range(math.ceil(prime_candidate / 2) + 1):
        if num > 1 and math.floor(prime_candidate / num) == prime_candidate / num:
            return False

    return True


if __name__ == '__main__':
    while(True):
        user_number = input('enter a number to check: ')
        try:
            user_number = int(user_number)
            print(f'the number {user_number} is', ' prime' if is_prime(user_number) else ' not prime')
        except:
            print('enter a valid number')