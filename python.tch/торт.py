fin = open('INPUT.TXT')
line = fin.readline()
fin.close()
n = [int (i) for i in line.split()]
n=n[0]
if n%2==0:
    n= n//2
fout = open('OUTPUT.TXT', 'w')
fout.write(str(n))
fout.close()
