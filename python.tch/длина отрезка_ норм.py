def modul(a):
    if a>=0:
        return a
    return -a

def pifagor(a, b):
    return (a**2 + b**2)**0.5

def length_line(x1, y1, x2, y2):
    l1 = modul(x2 - x1)
    l2 = modul(y2 - y1)
    return pifagor(l1, l2)

x1, y1, x2, y2 = [int (i) for i in input().split()]
print(length_line(x1, y1, x2, y2))
