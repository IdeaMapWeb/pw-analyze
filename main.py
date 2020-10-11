import time
import getpass
from itertools import product

target = getpass.getpass(prompt='Enter Your Password')
chars = '0123456789abcdefghijklmnopqrstuvwxyz'

def check(text, repeat):
    passwords = product(text, repeat=repeat)
    for i, password in enumerate(passwords):
        print('\033[32m' + str(i) + ':' + ''.join(password) + '\033[0m')
        if ''.join(password) == target:
            return ''.join(password)

def yes_no_input():
    while True:
        choice = input('Going to start analyzing your password [y/N]: ').lower()
        if choice == 'y':
            return True
        else:
            return False

if yes_no_input():
    start = time.time()
    pw = check(chars, 6)

    if pw is None:
        print('failure')
    else:
        print('cannot find pw --->', pw)
    finish = time.time() - start
    print(finish, '秒')

else:
    print('Program End')

