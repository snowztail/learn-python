import sys

if len(sys.argv) != 3:
    raise TypeError("Need 2 arguments, but ", str(len(sys.argv) - 1), " were provided.")

try:
    numerator = float(sys.argv[1])
except TypeError:
    raise TypeError("Argument 1 cannot be converted to float.")

try:
    denominator = float(sys.argv[2])
except TypeError:
    raise TypeError("Argument 2 cannot be converted to float.")

print(numerator / denominator)
