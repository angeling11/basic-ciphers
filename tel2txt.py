#!/usr/bin/python3

import sys

keyboard = {
        "0": [" "],
        "1": [""],
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["G", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y", "Z"]
}

if len(sys.argv) > 1:
        inp = sys.argv[1]
else:
        inp = sys.stdin.read()

out = ""
n = 0

while n < len(inp):
        if inp[n].isnumeric():
                i = 0
                aux = inp[n]
                while inp[n] == aux:
                        i += 1
                        n += 1
                out += keyboard[aux][i - 1]
        else:
                out += inp[n]
                n += 1

print("Text Decoded:")
print(out)
