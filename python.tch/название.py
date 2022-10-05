fin = open("INPUT.TXT")
line = fin.readline()
fin.close()
a, b=[int (i) for i in line.split()]
fout = open('OUTPUT.TXT', 'w')
fout.write(str(a+b))
fout.close()