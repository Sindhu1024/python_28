def input1():
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    c=int(input("Enter third number"))
    return a,b,c
def compare(a,b,c):
    if(a>b and a>c):
        print("{0} is the greatest number among {0},{1} and {2}".format(a,b,c))
    elif(b>a and b>c):
        print("{0} is the greatest number among {1},{0} and {2}".format(b,a,c))
    else:
        print("{0} is the greatest number among {1},{2} and {0}".format(c,a,b))

def main():
    x,y,z=input1()
    compare(x,y,z)
main()

#def input1():
 #   a=int(input("Enter first number"))
 #  b=int(input("Enter second number"))
 # c=int(input("Enter third number"))
 #return a,b,c
#def great_terenery(a,b,c):
   #max=print(a) if a>b and a>c else print(b) if b>c else print(c)
#def main():
    #x,y,z=input1()
    #great_terenery(x,y,z)
#main()
