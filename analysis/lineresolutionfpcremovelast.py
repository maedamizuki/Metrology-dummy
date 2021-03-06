import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import re

skip_words = ['CX', 'WX','WY','WZ']

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE1.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip = [line.strip() for line in lines]
X1 = [line for line in lines_strip if 'X' in line]
Y1 = [line for line in lines_strip if 'Y' in line]
Z1 = [line for line in lines_strip if 'Z' in line]

X2 = []
Y2 = []
Z2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

X2 = [float(s) for s in re.findall(pattern,str(X1))]
Y2 = [float(s) for s in re.findall(pattern,str(Y1))]
Z2 = [float(s) for s in re.findall(pattern,str(Z1))]
print(X2)

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE2.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

resolutionx = []
resolutiony = []
print(len(XX2))
for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE3.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))


path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE4.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE5.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE6.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE7.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE8.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]


for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE9.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))


path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE10.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==11 or i==12 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==25:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))


path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE11.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(sys.argv[1],'r',encoding='shift_jis') as f1:
   lines = f1.readlines()

lines_strip2 = [line.strip() for line in lines]
XX1 = [line for line in lines_strip2 if 'X' in line]
YY1 = [line for line in lines_strip2 if 'Y' in line]
ZZ1 = [line for line in lines_strip2 if 'Z' in line]

XX2 = []
YY2 = []
ZZ2 = []

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

for i in range(len(XX2)):
   if i==0 or i==1 or i==4 or i==7 or i==10 or i==13 or i==16 or i==19 or i==22:
      continue
   if i==23:
      break
   resolutionx.append("{:.20f}".format(XX2[i]-X2[i]))
   resolutiony.append("{:.20f}".format(YY2[i]-Y2[i]))


print(resolutionx)
fig = plt.figure()
plt.title('resolution x')
plt.xlabel('x[mm]')
plt.ylabel('events')
plt.hist(resolutionx,bins=100,range=(-0.1,0.1))
plt.show()

print(resolutiony)
fig2 = plt.figure()
plt.title('resolution y')
plt.xlabel('y[mm]')
plt.ylabel('events')
plt.hist(resolutiony,bins=100,range=(-0.1,0.1))
plt.show()

f = open(sys.argv[2],'w')
f.write(str(resolutionx))
f.close()
f = open(sys.argv[3],'w')
f.write(str(resolutiony))
f.close()

#g2.SetTitle("SETUP via dy coordinate;#Delta y[mm];event")
#g2.SetMarkerStyle(20)
#g2.SetMarkerSize(1)
#cv2.cd()
#g2.Draw()
#cv2.SaveAs("../../plot/0801/SETUPdycoordinate.root")
