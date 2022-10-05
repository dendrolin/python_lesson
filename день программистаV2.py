def year(y):
    if y % 400 == 0 or y%4==0 and y%100!=0:
        return f"12/09/{y:04d}"
    return f"13/09/{y:04d}"
y = int(input())
print(year(y))