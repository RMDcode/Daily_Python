def Add(no1,no2):
    return no1+no2

Addx = lambda no1,no2 : no1 + no2
    
def CheckEven(no):
    return (no%2==0)

Evenx=lambda no : no%2==0


def Increase(no):
    return no+2

Increasex= lambda no : no+2

def main():
    Ret=Add(10,11)
    print(Ret)
    Ret=CheckEven(10)
    print(Ret)
    Ret=Increase(10)
    print(Ret)

    print("Output from lambda function")

    Ret=Addx(10,11)
    print(Ret)
    Ret=Evenx(10)
    print(Ret)
    Ret=Increasex(10)
    print(Ret)

if __name__=="__main__":
    main()