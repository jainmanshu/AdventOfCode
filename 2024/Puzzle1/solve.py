import heapq
import collections

with open('input_1.txt') as f:
    parsed = f.read().splitlines()

# solved via either sorting the array or use heap
# we will use heap

q1, q2 = [], []

for line in parsed:
    n1, n2 = line.split()
    heapq.heappush(q1, int(n1))
    heapq.heappush(q2, int(n2))

# For Part-2 
# we can use counter class from defaultdict
# get the counter from second list
# loop the first list as key in second
freq = collections.Counter(q2)
result2 = 0

for num in q1:
    if num in freq:
        result2 += num * freq[num]

print("Answer Puzzle 2:", result2)

# Part - 1
result1 = 0

while q1 and q2:
    # Get the smallest from both and add it to res
    num1 = heapq.heappop(q1)
    num2 = heapq.heappop(q2)
    result1 += abs(num1-num2)

print("Answer Puzzle 1:", result1)



