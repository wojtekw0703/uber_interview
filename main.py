#Written by wojtekw0703
#Interview task asked by Uber
array = [1,2,3,4,5]
result_array = []
result_number = 1

for i in range(len(array)):
    for z in range(len(array)):
        if z==i:
            continue
        else:
         result_number *= array[z]
    result_array.append(result_number)
    result_number = 1

print(result_array)
