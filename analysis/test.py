import math
import numpy as np

Z=13.0
A=Z-3
E=60.0
B=5.5/(Z+5)+1.06
S = 1/(1+5.184*10**(-3)*A**(0.8107)*(E/100)**(-1*B))
a=E/511
sigma = 0.49893*((1+a)/a**2*((2*(1+a))/(1+2*a)-(1/a)*np.log(1+2*a)+(1/(2*a))*np.log(1+2*a)-(1+3*a)/(1+2*a)**2))

output=Z*S*sigma
print(output)
