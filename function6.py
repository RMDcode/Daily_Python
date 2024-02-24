#Function accepts multiple parameter and return multiple parameter
def Marvellous(value1,value2):
    Addition=value1+value2
    Substraction=value1+value2
    Multiplication=value1*value2
    Division=value1/value2

    return Addition,Substraction,Multiplication,Division

def main():
    Ret=Marvellous(11,6)
    print("Addition is:",Ret[0])
    print("Substraction is:",Ret[1])
    print("Multiplication is:",Ret[2])
    print("Division",Ret[3])

if __name__=="__main__":
    main()