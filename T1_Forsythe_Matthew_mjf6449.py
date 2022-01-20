'''
Full Name: Matthew Forsythe
ID: 907213659
Date: 1/20/2022
Filename: T1_Forsythe_Matthew_mjf6449.py
Purpose: The purpose of this code is to calcualte the gravitational force between two masses
'''

G=(6.67*(10**(-11)))#Gravitational Constant
m1=(3.0*(10**(8)))#Mass of mass one in kg
m2=(1.9*(10**(8)))#Mass of mass two in kg
r=60#Distance between two masses in meters

F=(G*m1*m2)//(r**2)#Equation for Newton's law of gravitation

print("The attractive force is", F)#Print line for the force between the two masses
