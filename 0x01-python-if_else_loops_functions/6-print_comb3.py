#!/usr/bin/python3
# i represents first digit and j reps second digit

for i in range(10):
    for j in range(i + 1, 10):
        print("{0}{1}".format(i, j), end="")
        if i == 8 and j == 9:
            print("")
        else:
            print(", ", end="")
