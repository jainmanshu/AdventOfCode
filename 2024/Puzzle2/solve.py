with open('input_1.txt') as f:
    reports = f.read().splitlines()

# safe levels either increasing or decreasing 
# atleast by 1 and atmost by 3
def part1(reports):
    count = 0
    for report in reports:
        report = list(map(int, report.split()))
        if report != sorted(report) and report != sorted(report, reverse=True):
            continue
        N = len(report)
        report.sort()
        good = True
        for i in range(1, N):
            diff = abs(report[i] - report[i-1])
            if not (1 <= diff <= 3):
                good = False
        if good:
            count += 1
    return count

def part2(reports):
    count = 0
    for report in reports:
        report = list(map(int, report.split()))
        is_good = False
        for i in range(len(report)):
            nums = report[:i] + report[i+1:]

            if nums != sorted(nums) and nums != sorted(nums, reverse=True):
                continue
            nums.sort()
            good = True
            for x, y in zip(nums, nums[1:]):
                if not (1 <= abs(x-y) <= 3):
                    good = False
            if good:
                is_good = True
        if is_good:
            count += 1
    return count

print("Answer Puzzle 1:", part1(reports))
print("Answer Puzzle 2:", part2(reports))