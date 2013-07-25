if __name__=="__main__":
    n = int(raw_input("How many fibonacci number: "))
    a = 1
    b = 1
    if n < 1:
        quit()
    if n == 1:
        print a
    elif n == 2:
        print a
        print b
    else:
        print a
        print b
        for i in range(0,n-2):
            a,b = b, a+b
            print b
