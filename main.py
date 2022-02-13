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
    for index in range(100):
        if is_prime(index):
            print(f'the number {index} is prime')
        else:
            print(f'the number {index} is not prime')
