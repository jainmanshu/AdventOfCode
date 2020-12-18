from input1 import input_array

sizeArray = len(input_array) - 1

for i in range(0, sizeArray):
    for j in range(1, sizeArray):
        for k in range(2, sizeArray):
            if input_array[i] + input_array[j] + input_array[k] == 2020:
                print(input_array[i]*input_array[j]*input_array[k])
                break
print('none found')