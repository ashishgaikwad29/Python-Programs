# ============================================================
# Program 08 : Multiplication Table of 5
# ============================================================

# Problem Statement:
# Write a Python program to print the multiplication
# table of 5 using a while loop.
#
# Example Output:
#
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50
# ============================================================

count = 1

while count <= 10:
    print("5 x", count, "=", 5 * count)
    count = count + 1