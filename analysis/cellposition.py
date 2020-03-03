import re 
import sys
import math

def main():

    skip_words = ['CX','WX','WY','WZ']
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
#    print(X2)
#    exit()
   #calculate the dimension between the line and the point
    d1 = X2[0]
    d2 = Y2[1]
    d3 = X2[2]
    d4 = Y2[3]
    print("d1=",d1,"d2=",d2,"d3=",d3,"d4=",d4)
   


main()
