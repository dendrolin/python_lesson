fin = open('INPUT.TXT')
line = fin.readline()
fin.close()
w, h, r = [int (i) for i in line.split()]
fout= open('OUTPUT.TXT', 'w')
if w >=r*2 and h >= r*2:
    fout.write('YES')
else:
    fout.write('NO')
fout.close()
