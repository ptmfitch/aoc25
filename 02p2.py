def calc_differences(report):
    differences = []
    for i in range(0, len(report) - 1):
        differences.append(report[i] - report[i + 1])
    return differences

def is_safe(differences):
    for difference in differences:
        if differences[0] < 0:
            if difference >= 0:
                # print("Positive or zero distance in an increasing report: {}".format(differences))
                return False
        elif differences[0] > 0:
            if difference <= 0:
                # print("Negative or zero distance in a decreasing report: {}".format(differences))
                return False
        else:
            # print("Zero distance on first step: {}".format(differences))
            return False
        if difference > 3 or difference < -3:
            # print("Step too big: {}".format(differences))
            return False
    return True


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
    if not is_safe(differences):
        temp = False
        for i in range(0, len(report)):
            temp_report = report.copy()
            temp_report.pop(i)
            temp_differences = calc_differences(temp_report)
            if is_safe(temp_differences):
                temp = True
                break
        if not temp:
            print("Not safe: {}".format(differences))
            safe -= 1
        else:
            print("Safe: {}".format(differences))
    else:
        print("Safe: {}".format(differences))

print("Result: {}".format(safe))