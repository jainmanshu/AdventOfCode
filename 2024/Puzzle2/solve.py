with open('input_1.txt') as f:
    reports = f.read().splitlines()

safe_reports = 0

# safe levels either increasing or decreasing 
# atleast by 1 and atmost by 3
def is_safe(report):
    N = len(report)
    is_inc = True if int(report[1]) > int(report[0]) else False
    for i in range(1, N):
        diff = int(report[i]) - int(report[i-1]) if is_inc else int(report[i-1]) - int(report[i])
        if not (0 < diff <= 3):
            return False
    return True

for report in reports:
    if is_safe(report.split()):
        safe_reports += 1

print("Answer Puzzle 1:", safe_reports)