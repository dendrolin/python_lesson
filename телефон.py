def telephone(a, b, c, t):
    if t <= a:
        return b * t
    return a * b + (t - a) * c
a, b, c, t = [int (i) for i in input().split()]
print(telephone(a, b, c, t))