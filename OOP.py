class Arithematic:
    def __init__(self,A,B):
        print("Inside Constructor")
        self.no1=A
        self.no2=B

    def Addition(self):
        Ans=0
        Ans=self.no1+self.no2
        return Ans

    def Substraction(self):
        Ans=0
        Ans= self.no1-self.no2
        return Ans


def main():

    value1=int(input("Enter first number :"))
    value2=int(input("Enter first number :"))
    
    obj1=Arithematic(value1,value2)
    ret=obj1.Addition()
    print("Addition is :",ret)

    ret=obj1.Substraction()
    print("Substraction is :",ret)

    
    value1=int(input("Enter first number :"))
    value2=int(input("Enter first number :"))
    
    obj2=Arithematic(value1,value2)
    ret=obj2.Addition()
    print("Addition is :",ret)

    ret=obj2.Substraction()
    print("Substraction is :",ret)


if __name__=="__main__":
    main()