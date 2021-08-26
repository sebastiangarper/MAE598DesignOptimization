import scipy as sp
from scipy.optimize import minimize

f = lambda x: (x[0]-x[1])**2+(x[1]+x[2]-2)**2+(x[3]-1)**2+(x[4]-1)**2

cons = ({'type':'eq','fun': lambda x: x[0]+3*x[1]},
        {'type':'eq','fun': lambda x: x[2]+x[3]-2*x[4]},
        {'type':'eq','fun': lambda x: x[1]-x[4]})
bnds = ((-10,10),(-10,10),(-10,10),(-10,10),(-10,10))
res = minimize(f,(0,0,0,0,0),bounds=bnds, constraints=cons)

# minimum point of the function
print(res)