with open('input_9.txt') as f:
    lines = f.read().splitlines()

# print(lines)

lines_int = [int(i) for i in lines]

# print(lines_int)

def checkWheterNumber(numberArray, targetSum): 
    for i in range(len(numberArray)):
        for j in range(i+1, len(numberArray)):
            if numberArray[i] + numberArray[j] == targetSum:
                return True
            if (i == j): return False
    return False


# print(checkWheterNumber(inputTest, preambleLength))

def findNumber(inp, preambleLength):
    for i in range(len(inp)):
        inputArray = inp[i:i+preambleLength]
        target = inp[i+preambleLength]
        if checkWheterNumber(inputArray, target):
            continue
        else:
            return target
        
result = findNumber(lines_int, 25)
print("result", result)


# def findSet(inp, target, partial = []):
#     s = sum(partial)
#     if s == target:
#          print('sum', target, partial)
#     if s > target:
#         return
    
#     for i in range(len(inp)):
#         n = inp[i]
#         remaining = inp[i+1:]
#         findSet(remaining, target, partial + [n])

# sample = [25, 47, 40, 62, 55, 65, 95, 102]
# out = 127
# print(findSet(lines_int, out))

def subArray(arr, n, target): 
  
    # Pick starting point 
    for i in range(0,n): 
  
        # Pick ending point 
        for j in range(i,n): 
            sum1 = sum(arr[i:j+1])
            if(sum1 == target): return arr[i:j+1]
 

answer_subArray = subArray(lines_int, len(lines_int), result)
print('Answer Subarray', answer_subArray)

minNumber = min(answer_subArray)
print('Min Numner', minNumber)
maxNumber = max(answer_subArray)
print('MaxNumber', maxNumber)

FinalSum = minNumber + maxNumber

print('FinalSum', FinalSum)


