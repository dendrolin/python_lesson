fin = open('INPUT.TXT')
line = fin.readline()
fin.close()
x, y, z= [int (i) for i in line.split()]
s= x+y-z
fout = open('OUTPUT.TXT', 'w')
if s<0: 
    fout.write('Impossible')
else:
    fout.write(str(s))
fout.close()