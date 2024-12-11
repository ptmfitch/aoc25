sample_input = '0 1 10 99 999'
longer_sample_input = '125 17'
personal_input = '20 82084 1650 3 346355 363 7975858 0'

input = personal_input
print('Input:', input)
print()

blinks = 25
print('Blinks to process:', blinks)
print()

stones = input.rstrip().split(' ')
print('Initial arrangement:')
print(' '.join(stones))
print()

for b in range(0, blinks):
    new_stones = []
    for i in range(0, len(stones)):
        s = stones[i]
        if s == '0':
            new_stones.append('1')
        elif len(s) % 2 == 0:
            l = int(len(s) / 2)
            new_stones.append(s[:l])
            new_stones.append(str(int(s[l:])))
        else:
            new_stones.append(str(int(s) * 2024))
    stones = new_stones
    print('After {} blink(s):'.format(b + 1))
    print(' '.join(stones))
    print()

print('Stones after {} blinks:'.format(blinks))
print(len(stones))
print()