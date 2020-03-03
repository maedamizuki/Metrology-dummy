import re 
import sys

def main():

    with open(sys.argv[1],'r',encoding='shift_jis') as f:
        lines = f.readlines()

    f = open(sys.argv[2],'w')


    x_list=[]
    y_list=[]
    data1=[]

    for line in lines:
        data = line[:-1].split(' ')
        x_list.append(float(data[0]))
        y_list.append(float(data[1]))

    x0= x_list[1]
    y0=y_list[1]
    n = 6000
    i = 0
    a = 0
    print(x0,y0)

    for i in range(n):
        
        for a in range(n):
            f.write(str(x0)+' '+str(y0)+'\n')
            y0=y0+1.0/3.0
            if y0>25.0:
                break
        x0=x0+1.0/3.0
        y0=y_list[1]
        if x0>33.2:
            break


main()
