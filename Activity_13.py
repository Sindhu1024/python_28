def inp(): 
    s=int(input("Enter the start number"))
    e=int(input("Enter the stop number"))
    return s,e
def odd(s,e):
    for i in range(s,e+1):
        if i%2 !=0:
            print(i)
def main():
    p,q=inp()
    odd(p,q)
main()

#s=int(input("Enter the start number"))
#e=int(input("Enter the stop number"))
#for i in range(s,e+1):
 #   if i%2 !=0:
 #       print(i)
        
        
#s=int(input("Enter the start number"))
#e=int(input("Enter the stop number"))
#a=list(range(s,e+1,2))
#print(a)
