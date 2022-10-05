data = [int(item) for item in input(). split()]
for index in range(1, len(data)):
    if data[index]*data[index-1]>0:
        print(data[index-1], data[index])
        break