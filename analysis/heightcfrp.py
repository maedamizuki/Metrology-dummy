import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy import linalg
#import ROOT
#from ROOT import TCanvas,TH1F,gStyle
import sys
import re
from io import open

#path = '/Users/maedamizuki/metrology/1004/MEASURE5.TXT'
#file = open(sys.argv[1])
def main():
   with open(sys.argv[1],'r',encoding='shift_jis') as f1:
      lines = f1.readlines()
   lines_strip = [line.strip() for line in lines]
   X1 = [line for line in lines_strip if 'X' in line]
   Y1 = [line for line in lines_strip if 'Y' in line]
   Z1 = [line for line in lines_strip if 'Z' in line]
   print(X1)
   X2 = []
   Y2 = []
   Z2 = []

   pattern=r'([+-]?[0-9]+\.?[0-9]*)'

   X2 = [float(s) for s in re.findall(pattern,str(X1))]
   Y2 = [float(s) for s in re.findall(pattern,str(Y1))]
   Z2 = [float(s) for s in re.findall(pattern,str(Z1))]
   print(X2)
   X3=[]
   Y3=[]
   Z3=[]
   X3.extend([X2[0],X2[1],X2[2],X2[3]])
   Y3.extend([Y2[0],Y2[1],Y2[2],Y2[3]])
   Z3.extend([Z2[0],Z2[1],Z2[2],Z2[3]])
#X22 = np.square(X2)
#Y22 = np.square(Y2)
   point_list=[X3,Y3]
   X = np.array(point_list).T
   Z = np.array(Z3)
   Xtil = np.c_[np.ones(X.shape[0]),X]
   A = np.dot(Xtil.T,Xtil)
   b = np.dot(Xtil.T,Z)
   w = linalg.solve(A,b)
   print(w[0],w[1],w[2])
   ZT = np.array(Z3).T
   dis = ZT*Z
#print(dis)
   xmesh, ymesh = np.meshgrid(np.linspace(-20,20,20),np.linspace(-15,25,20))
   zmesh = (w[0]+w[1]*xmesh.ravel()+w[2]*ymesh.ravel()).reshape(xmesh.shape)



#3d plot code
   fig = plt.figure()
   ax  = fig.add_subplot(111,projection='3d')
   p=ax.scatter(X2,Y2,Z2,s=5,c=Z2,cmap=plt.cm.jet)
   plt.colorbar(p)
   p=ax.plot_wireframe(xmesh,ymesh,zmesh,color='c')

#ax.text(-20,-20,0.09,"a="+str(w[0])+"\n"+"b="+str(w[1])+"\n"+"c="+str(w[2]),size=10,color='k')
   p=ax.set_xlabel("x[mm]")
   p=ax.set_ylabel("y[mm]")
   p=ax.set_zlabel("z[mm]")

   dis = Z - np.dot(Xtil,w)
   dis1 = np.square(dis)
   E = sum(dis1)
#   plt.show()
#print(dis)
#print(E)
   #calculate the height
   xfpc = (X2[4]+X2[5]+X2[6]+X2[7])/4
   yfpc = (Y2[4]+Y2[5]+Y2[6]+Y2[7])/4
   zfpc = (Z2[4]+Z2[5]+Z2[6]+Z2[7])/4
   diss1=(-zfpc+w[1]*xfpc+w[0]+w[2]*yfpc)/math.sqrt(w[1]**2+w[2]**2+(1.0)**2)
   print(diss1)
   plt.show()

   resolutionplane=[]
   for i in range(4):
      diss2=(-Z2[i]+w[1]*X2[i]+w[0]+w[2]*Y2[i])/math.sqrt(w[1]**2+w[2]**2+(1.0)**2)
      resolutionplane.append(diss2)
   print(resolutionplane)

#ROOT code
#   cv = TCanvas("cv","c1",850,600)
#   cv.Divide(2,2)
#   g1 = TH1F("h2","FlexModule",50,-0.1,0.1)

#   for i in xrange(len(Z2)):
#      diss = 0.0
#      diss = Z2[i]-(w[0]+w[1]*X2[i]+w[2]*Y2[i])
#      g1.Fill(diss)
#      i+=1
#   g1.SetTitle("flatness;#Delta z[mm];events")
#   g1.SetMarkerStyle(20)
#   g1.SetMarkerSize(1)
#   cv.cd(1)
#   g1.Draw("")
#   g1.Fit("gaus","i")
#   gStyle.SetStatH(0.15)
#   gStyle.SetStatW(0.15)
#   gStyle.SetOptFit(1)


#   distotal=0.0                 

#   g4 = TH1F("h4","SSR",50,0,0.005)
#   for i in xrange(len(Z2)):
#      dis2 =0.0
#      dis=0.0
#      dis = Z2[i]-(w[0]+w[1]*X2[i]+w[2]*Y2[i])
#      dis2 = dis*dis
#      g4.Fill(dis2)
#      distotal = distotal+dis2
#      i+=1
#   print math.sqrt(distotal/i),i
#   g4.SetTitle("SSR;[mm^2];events")
#   g4.SetMarkerStyle(20)
#   g4.SetMarkerSize(1)
#   cv.cd(2)
#   g4.Draw("")


#print(diss)

#   cv2 = TCanvas("cv2","c2",850,600)
#   g2 = TH1F("h2","flatness",50,0,0.1)
   
#   for i in xrange(len(Z2)):
#      diss1 = 0.0
#      diss1 = abs(-Z2[i]+w[1]*X2[i]+w[0]+w[2]*Y2[i])/math.sqrt((w[1])**2+(w[2])**2+(1.0)**2)
#      g2.Fill(diss1)
#      i+=1
#   g2.SetTitle("Flatness;#Delta d[mm];events")
#   g2.SetMarkerStyle(20)
#   g2.SetMarkerSize(1)
#   cv.cd(3)
#   g2.Draw("")


#   cv3 = TCanvas("cv3","c3",850,600)
#   g3 = TH1F("h2","flatness",50,-0.1,0.1)
   
#   for i in xrange(len(Z2)):
#      diss1 = 0.0
#      diss1 = (-Z2[i]+w[1]*X2[i]+w[0]+w[2]*Y2[i])/math.sqrt((w[1])**2+(w[2])**2+(1.0)**2)
#      g3.Fill(diss1)
#      i+=1
   #print(diss1)
#   g3.SetTitle("Flatness;#Delta d[mm];events")
#   g3.SetMarkerStyle(20)
#   g3.SetMarkerSize(1)
#   cv.cd(4)
#   g3.Draw("")
#   g3.Fit("gaus","i")
#   gStyle.SetStatH(0.15)
#   gStyle.SetStatW(0.15)
#   gStyle.SetOptFit(1)#


#   cv.SaveAs("test.png")

main()
