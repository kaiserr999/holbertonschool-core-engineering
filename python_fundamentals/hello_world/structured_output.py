#!/usr/bin/env python3

# Derive float from numeric value and format to two decimals
pi_approx = round(22 / 7, 2)

# Boolean from comparison expression
is_valid = pi_approx == 3.14

# Output using formatted string interpolation
print(f"Language: Python")
print("Version: 3")
print(f"Pi approx: {pi_approx:.2f}")
print(f"Computation valid: {is_valid}")