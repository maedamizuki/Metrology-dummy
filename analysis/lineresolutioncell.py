import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import re

skip_words = ['CX', 'WX','WY','WZ']

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE1.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE2.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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
resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE3.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE4.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE5.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE6.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE7.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE8.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE9.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE10.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

path = '/Users/maedamizuki/metrology/dummy/data/lineresolutioncellside/LINE11.TXT'

with open(path,'r',encoding='shift_jis') as oldfile, open(sys.argv[1],'w',encoding='shift_jis') as newfile:
   for line in oldfile:
      if not any(skip_word in line for skip_word in skip_words):
         newfile.write(line)
with open(path,'r',encoding='shift_jis') as f1:
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

resolutionx.extend([XX2[2]-X2[2],XX2[3]-X2[3],XX2[5]-X2[5],XX2[6]-X2[6],XX2[8]-X2[8],XX2[9]-X2[9],XX2[11]-X2[11],XX2[12]-X2[12],XX2[14]-X2[14],XX2[15]-X2[15],XX2[17]-X2[17],XX2[18]-X2[18],XX2[20]-X2[20],XX2[21]-X2[21],XX2[23]-X2[23],XX2[24]-X2[24]])
resolutiony.extend([YY2[2]-Y2[2],YY2[3]-Y2[3],YY2[5]-Y2[5],YY2[6]-Y2[6],YY2[8]-Y2[8],YY2[9]
-Y2[9],YY2[11]-Y2[11],YY2[12]-Y2[12],YY2[14]-Y2[14],YY2[15]-Y2[15],YY2[17]-Y2[17],YY2[18]-Y2[18],YY2[20]-Y2[20],YY2[21]-Y2[21],YY2[23]-Y2[23],YY2[24]-Y2[24]])

print(len(resolutionx))
fig = plt.figure()
plt.title('resolution x')
plt.xlabel('x[mm]')
plt.ylabel('events')
plt.hist(resolutionx,bins=100,range=(-0.1,0.1))
plt.show()

print(len(resolutiony))
fig2 = plt.figure()
plt.title('resolution y')
plt.xlabel('y[mm]')
plt.ylabel('events')
plt.hist(resolutiony,bins=100,range=(-0.1,0.1))
plt.show()



#g2.SetTitle("SETUP via dy coordinate;#Delta y[mm];event")
#g2.SetMarkerStyle(20)
#g2.SetMarkerSize(1)
#cv2.cd()
#g2.Draw()
#cv2.SaveAs("../../plot/0801/SETUPdycoordinate.root")
