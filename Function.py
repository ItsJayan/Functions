def SwapFileData():
    f1=input("enter the first file name to swap")
    f2=input("enter the second file name to swap")

    with open(f1,'r')as a:
        data_a=a.read()
        
    with open (f2,'r')as b:
        data_b=b.read()

    with open (f1,'w')as a:
        a.write(data_b)

    with open (f2,'w')as b:
        b.write(data_a)
SwapFileData()