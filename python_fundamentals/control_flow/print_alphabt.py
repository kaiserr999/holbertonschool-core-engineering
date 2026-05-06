#!/usr/bin/env python3
output = ""
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        output += chr(i)
print("{}".format(output))