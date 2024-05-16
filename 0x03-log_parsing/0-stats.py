#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET
"""
import sys


def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
my_lines = 0
my_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            my_lines += 1

            if count_lines <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in my_codes.keys()):
                    my_codes[code] += 1

            if (count_lines == 10):
                print_msg(my_codes, file_size)
                my_lines = 0

finally:
    print_msg(my_codes, file_size)
