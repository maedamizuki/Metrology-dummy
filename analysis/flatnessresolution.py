import math
import numpy as np
import matplotlib.pyplot as plt
import glob
import sys
import re
import pandas
from decimal import Decimal

#path = '/Users/maedamizuki/metrology/dummy/data/flatnesszresolution/4.TXT'
def main():
   np.set_printoptions(suppress=True)
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

#path = '/Users/maedamizuki/metrology/dummy/data/flatnesszresolution/1.TXT'

   file_list= glob.glob("/Users/maedamizuki/metrology/dummy/data/meeting/*")
   resolution =[]
   print(file_list)

   for i in range(len(file_list)):
      if i==1:
      #   print("first ok")
         continue
      print("OK")
      with open(file_list[i],'r',encoding='shift_jis') as f2:
         lines2 = f2.readlines()
      lines_strip2 = [line.strip() for line in lines2]
      XX1 = [line for line in lines_strip2 if 'X' in line]
      YY1 = [line for line in lines_strip2 if 'Y' in line]
      ZZ1 = [line for line in lines_strip2 if 'Z' in line]
      print(ZZ1)
      XX2 = []
      YY2 = []
      ZZ2 = []

      pattern=r'([+-]?[0-9]+\.?[0-9]*)'

      XX2 = [float(s) for s in re.findall(pattern,str(XX1))]
      YY2 = [float(s) for s in re.findall(pattern,str(YY1))]
      ZZ2 = [float(s) for s in re.findall(pattern,str(ZZ1))]

      print(i,len(ZZ2))
      for d in range(len(X2)):
         d1=Z2[d]-ZZ2[d]
         #         '{:.40g}'.format(d1)
         resolution.append(Decimal(d1))
         print(Decimal(d1))
         d1 =0.0
   print(len(resolution))

   f = open(sys.argv[2],'w')
   f.write(str(resolution))
   f.close()

main()

#g2.SetTitle("SETUP via dy coordinate;#Delta y[mm];event")
#g2.SetMarkerStyle(20)
#g2.SetMarkerSize(1)
#cv2.cd()
#g2.Draw()
#cv2.SaveAs("../../plot/0801/SETUPdycoordinate.root")
