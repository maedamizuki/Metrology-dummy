import re 
import sys

def main():

    #with open(sys.argv[1],'r',encoding='shift_jis') as f:
    #    lines = f.readlines()

    f = open(sys.argv[1],'w')


    x_list=[]
    y_list=[]
    data1=[]
    x_start = -2.33699
    y_start = -1.905
    n=10000;
    step = 1.5
    i=0
    for i in range(n):
        
        x_list.append(x_start)
        y_list.append(y_start)
        x_start= x_start+step
        y_start = y_start+step
        if y_start > 25 and x_start>33.2:
            break
    
            
        '''
        data = line[:-1].split(' ')
        x_list.append(float(data[0]))
        y_list.append(float(data[1]))
        '''
    x0= x_list[1]
    y0=y_list[1]
    n = 6000
    i = 0
    a = 0
    print(x0,y0)

    for i in range(len(x_list)):
        
        if i%2==0:
            for a in range(len(y_list)):
                f.write(str(x_list[i])+' '+str(y_list[a])+'\n')
                if y_list[a]>25:
                    break
        if i%2==1:
            for a in range(len(y_list)):
                f.write(str(x_list[i])+' '+ str(y_list[-a-1])+'\n')
                if a==len(y_list):
                    break
                if y_list[a]>25:
                    break
        if x_list[i]>33.2:
            break


main()
