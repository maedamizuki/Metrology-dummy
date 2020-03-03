import re
import sys

def main():

   with open(sys.argv[1],'r',encoding='shift_jis') as f:
      lines = f.readlines()

   f = open(sys.argv[2],'w')

   x_list=[]
   y_list=[]
   data1=[]
#   x0=2.63
#   y0=9.70

   for line in lines:
      data = line[:-1].split(' ')
      x_list.append(float(data[0]))
      y_list.append(float(data[1]))
   
   i=1
   n=100
   k=298
   for i in range(n-1):
      data1=[i+k]
      print(data1)
      f.write('Measure.Point Label:=\"point'+str(data1[0])+'\"\nStage.MoveTo X:='+str(x_list[i+k]-x_list[0])+', Y:='+str(y_list[i+k]-y_list[0])+', Z:=0\nFocusTool.Run X:='+str(x_list[i+k]-x_list[0])+', Y:='+str(y_list[i+k]-y_list[0])+', Z:=0, W:=0.3, H:=0.3\nMeasure.EndMeas\nResults.ReportFeature Show:=X_ and Y_ and Z_, Tag:=\"point'+str(data1[0])+'\"\n')

      print
#      f.write()

main()
