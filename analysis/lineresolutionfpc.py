import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import glob


def main():

   skip_words = ['CX', 'WX','WY','WZ']

   #path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE1.TXT'
   
   with open(sys.argv[1],'r',encoding='shift_jis') as oldfile, open(sys.argv[2],'w',encoding='shift_jis') as newfile:
      for line in oldfile:
         if not any(skip_word in line for skip_word in skip_words):
            newfile.write(line)
   with open(sys.argv[2],'r',encoding='shift_jis') as f1:
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

   #path = '/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/LINE2.TXT'
   file_list = glob.glob("/Users/maedamizuki/metrology/dummy/data/lineresolutionfpcside/*")
   print(file_list)
   resolutionx = []
   resolutiony = []
   for i in range(len(file_list)):
      if i==0:
         continue
      print("OK")

      with open(file_list[i],'r',encoding='shift_jis') as oldfile, open(sys.argv[2],'w',encoding='shift_jis') as newfile:
         for line in oldfile:
            if not any(skip_word in line for skip_word in skip_words):
               newfile.write(line)
      with open(sys.argv[2],'r',encoding='shift_jis') as f1:
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

      #print(len(XX2))
      for d in range(len(XX2)):
         if d==0 or d==1 or d==4 or d==7 or d==10:
            continue
         if d==13:
            break
         resolutionx.append(XX2[d]-X2[d])
         resolutiony.append(YY2[d]-Y2[d])
         
   print(resolutionx)
   print(len(resolutionx))
   f = open(sys.argv[3],'w')
   f.write(str(resolutionx))
   f.close()
   
   f2 = open(sys.argv[4],'w')
   f2.write(str(resolutiony))
   f2.close()

main()

#g2.SetTitle("SETUP via dy coordinate;#Delta y[mm];event")
#g2.SetMarkerStyle(20)
#g2.SetMarkerSize(1)
#cv2.cd()
#g2.Draw()
#cv2.SaveAs("../../plot/0801/SETUPdycoordinate.root")
