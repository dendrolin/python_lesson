data = [int(item) for item in input(). split()]
for index, item in enumerate (data):
    if item%2==0:
        print(item, end=" ")