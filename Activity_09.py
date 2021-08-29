import math
l=float(input("Enter the lenght of the tromboloid"))
b=float(input("Enter the breadth of the tromboloid"))
h=float(input("Enter the height of the tromboloid"))
k=(l**2)+(b**2)+(h**2)
a=(b**2)*(h**2)
volume=a/(k**.5)
v=round(volume,3)
print("The volume is:",v)
r2=volume*.75
c=math.pi
r1=r2/c
r=(r1)**(1/3)
radius=round(r,3)
print("The radius of the sphere is:",radius)
