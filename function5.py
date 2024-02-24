#Function accepts multiple parameter and return multiple parameter
def Marvellous(value1,value2):
    Addition=value1+value2
    Substraction=value1+value2
    Multiplication=value1*value2
    Division=value1/value2

    return Addition,Substraction,Multiplication,Division

def main():
    Ret1,Ret2,Ret3,Ret4=Marvellous(11,6)
    print("Addition is:",Ret1)
    print("Substraction is:",Ret2)
    print("Multiplication is:",Ret3)
    print("Division",Ret4)

if __name__=="__main__":
    main()