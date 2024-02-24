
#Function defines another function inside it(Inner Function)
def Marvellous(value1,value2):
    def Add(A,B):
        return A+B

    Ans=Add(value1,value2)
    return Ans

def main():
    ret=Marvellous(11,7)
    print("Addition is :",ret)


if __name__=="__main__":
    main()