fin = open('INPUT.TXT')
line = fin.readline()
fin.close()
n = int(line)
fout = open('OUTPUT.TXT', 'w')
if n==12 or n==1 or n==2:
    fout.write('Winter')
elif n==3 or n==4 or n==5:
    fout.write('Spring')
elif n==6 or n==7 or n==8:
    fout.write('Summer')
elif n==9 or n==10 or n==11:
    fout.write('Autumn')
else:
    fout.write('Error')
fout.close()