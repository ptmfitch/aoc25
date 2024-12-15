import re
from operator import mul

machines = []
with open('inputs/13.csv') as f:
    f.readline() # Skip the first line
    machines = ''.join(f.readlines()).split('\n\n')

def extract_numbers(s):
    return [int(x) for x in re.findall(r'\d+', s)]

total = 0
for machine in machines:
    lines = machine.split('\n')
    A = extract_numbers(lines[0])
    B = extract_numbers(lines[1])
    prize = extract_numbers(lines[2])
    cheapest = None
    for a in range(0, 100):
        for b in range(0, 100):
            end = [
                a * A[0] + b * B[0],
                a * A[1] + b * B[1],
            ]
            if end == prize:
                cost = a*3 + b*1
                if not cheapest or cost < cheapest:
                    cheapest = cost
    if cheapest:
        total += cheapest

print(total)
