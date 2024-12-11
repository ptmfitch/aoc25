from operator import mul, pow
from functools import reduce
import numpy as np

with open('inputs/07.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

correct = []
# 190: 10 19
for i in range(0, len(lines)):
    if i % 10 == 0:
        print("{}%".format(i / len(lines) * 100))
    line = lines[i]
    split = line.rstrip().split(':')
    target = int(split[0])
    operands = [int(x) for x in split[1].lstrip().split(' ')]
    # print(target, operands)

    if target == sum(operands):
        # print("All +")
        correct.append(target)
    elif target == reduce(mul, operands):
        # print("All *")
        correct.append(target)
    else:
        for i in range(0, pow(3, (len(operands) - 1))):
            ternary = np.base_repr(i, base=3)
            terstr = str(ternary).zfill(len(operands) - 1)
            # print(target, operands, terstr)
            cur = operands[0]
            for j in range(0, len(terstr)):
                c = terstr[j]
                next = operands[j + 1]
                if c == '0':
                    cur += next
                elif c == '1':
                    cur *= next
                elif c == '2':
                    cur = int(str(cur) + str(next))
                if cur > target:
                    break
            if cur == target:
                # print("Found:", bin)
                correct.append(target)
                break

print(correct)
print(sum(correct))