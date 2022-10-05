fin = open('INPUT.TXT')
line = fin.readline()
n = int(line)
a = 0
b = 0
for i in range(0, n):
    line = fin.readline()
    if int(line) ==1:
        a+=1
    else:
        b+=1
fin.close()
fout = open('OUTPUT.TXT', 'w')
if a<b:
   fout.write(str(a))
else:
   fout.write(str(b))