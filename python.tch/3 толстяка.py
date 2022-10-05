fin = open('INPUT.TXT')
line = fin.readline()
fin.close()
list_m=[int (i) for i in line.split()]
list_m.sort()
if list_m[0]< 94 or list_m[2]> 727:
    text = 'Error'
else:
    text = str(list_m[2])
fout = open('OUTPUT.TXT', 'w')
fout.write(text)
fout.close()
