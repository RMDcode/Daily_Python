def Addition(no1,no2):
    Ans=0
    Ans=no1+no2
    return Ans

def Substraction(no1,no2):
    Ans=0
    Ans=no1-no2
    return Ans


def main():
    value1=int(input("Enter first number"))
    value2=int(input("Enter first number"))
    
    ret=(value1+value2)
    print("Addition is :",ret)

    ret=(value1-value2)
    print("Substraction is :",ret)


if __name__=="__main__":
    main()