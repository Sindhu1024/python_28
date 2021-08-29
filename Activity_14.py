def inp(): 
    s=int(input("Enter a number"))
    return s
def prime(s):
    if s > 1:
        for i in range(2,s):
            if (s % i) == 0:
                print(s,"is not a prime number")
                break
        else:
            print(s,"is a prime number")
    else:
        print(s,"is not a prime number")
def main():
    p=inp()
    prime(p)
main()
