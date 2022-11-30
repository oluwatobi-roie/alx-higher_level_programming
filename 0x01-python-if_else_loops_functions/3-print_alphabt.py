#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if (chr(i) == 'q') | (chr(i) == 'e'):
        continue
    else:
        print(f'{chr(i):s}', end=')
