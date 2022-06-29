#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(10):
        if (first_num != second_num and first_num < second_num) and first_num < 9:
            if (first_num == 8 and second_num == 9):
                print('{0}{1}'.format(first_num, second_num))
            else:
                print('{0}{1}, '.format(first_num, second_num), end='')
