'''
Full Name: Matthew Forsythe
ID: 907213659
Date: 1/28/2022
Filename: L2.1_Forsythe_Matthew_mjf6449.py
Purpose: The purpose of this code is to calculate the number of dollars left after t number year
'''
def future_value(P,i,n,t):
    F=(P*(1+(i/n))**(n*t))
    return(F)

fv=future_value(10000,0.14,12,10)
print(format(fv,".2f"))

fv=future_value(12000,0.12,4,50)
print(format(fv,".2f"))

fv=future_value(100000,0.23,1,20)
print(format(fv,".2f"))
