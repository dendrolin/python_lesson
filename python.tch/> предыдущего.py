data = [int(item) for item in input(). split()]
for index in range(1, len(data)):
    if data[index]> data[index-1]:
         print(data[index], end=' ')