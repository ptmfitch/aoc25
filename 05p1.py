with open('inputs/05.csv') as f:
    f.readline() # Skip the first line
    lines = f.readlines()

before_blank = True
rules = []
updates = []
for line in lines:
    if line == "\n":
        before_blank = False
    elif before_blank:
        print(line)
        rules.append(line.rstrip())
    else:
        print(line)
        updates.append(line.rstrip())

print("Rules:")
[print(rule) for rule in rules]
print()

print("Updates:")
[print(update) for update in updates]
print()

pages = set([
    p
    for rule in rules
    for p in rule.split('|')
])

print("Pages:")
[print(page) for page in pages]
print()

docs = {}
for page in pages:
    ascendents = []
    descendents = []
    for rule in rules:
        if rule.startswith(page):
            descendents.append(rule.split('|')[1])
        elif rule.endswith(page):
            ascendents.append(rule.split('|')[0])
    docs[page] = {
        'ascendents': ascendents,
        'descendents': descendents,
    }

print("Docs:")
[print("{}: {}".format(doc, docs[doc])) for doc in docs]
print()

middle_nos = []
for update in updates:
    print("Update: {}".format(update))
    splitUpdate = update.split(',')
    valid = True
    for i in range(0, len(splitUpdate) - 1):
        higher = splitUpdate[i]
        lower = splitUpdate[i + 1]
        if lower in docs[higher]['ascendents']:
            print("Invalid: {} -> {}".format(higher, lower))
            valid = False
            break
        elif higher in docs[lower]['descendents']:
            print("Invalid: {} -> {}".format(higher, lower))
            valid = False
            break
        else:
            print("Valid: {} -> {}".format(higher, lower))
    if valid:
        middle_nos.append(int(splitUpdate[int((len(splitUpdate)) / 2)]))

print("Middle Nos:")
[print(middle_no) for middle_no in middle_nos]

print("Sum of middle nos:")
print(sum(middle_nos))
