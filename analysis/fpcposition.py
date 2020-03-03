import re 
import sys
import math

def main():

    skip_words = ['CX', 'WX','WY','WZ']

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

    #calculate between points of FPC and ASIC
    dx1=[]
    dy1=[]
    dx2=[]
    dy2=[]
    dx3=[]
    dy3=[]
    dx4=[]
    dy4=[]
    dx=[]
    dy=[]

    for i in range(1):
        dx.append((X2[i+1]-X2[5],X2[i+1]-X2[8],X2[i+1]-X2[11],X2[i+1]-X2[14]))
        dy.append((Y2[i+1]-Y2[5],Y2[i+1]-Y2[8],Y2[i+1]-Y2[11],Y2[i+1]-Y2[14]))
        i+=1

        print(dx,dy)

main()


