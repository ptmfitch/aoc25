reports = []
with open('inputs/02.csv') as f:
    f.readline() # skip the first line
    for line in f:
        reports.append([int(x) for x in line.split()])

safe = len(reports)

for report in reports:
    differences = []
    for i in range(0, len(report) - 1):
        differences.append(report[i] - report[i + 1])
    temp = True
    for difference in differences:
        if differences[0] < 0:
            if difference >= 0:
                print("Positive or zero distance in an increasing report: {}".format(differences))
                temp = False
                break
        elif differences[0] > 0:
            if difference <= 0:
                print("Negative or zero distance in a decreasing report: {}".format(differences))
                temp = False
                break
        else:
            print("Zero distance on first step: {}".format(differences))
            temp = False
            break
        if difference > 3 or difference < -3:
            print("Step too big: {}".format(differences))
            temp = False
            break
    if not temp:
        safe -= 1
    else:
        print("Safe: {}".format(differences))

print("Result: {}".format(safe))