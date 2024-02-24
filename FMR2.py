import functools

def CheckEven(No):
    if(No % 2 ==0):
        return True
    else:
        return False

def Increase(No):
    return No+2

def Add(A,B):
    return A+B


def main():
    Data=[]
    print("Enter number of elements :")
    size=int(input())
    print(Data)
    
    print("Enter the elements:")
    for i in range(size):
        value=int(input())
        Data.append(value)

    output=list(filter(CheckEven,Data))
    print(output)
    output1=list(map(Increase,output))
    print(output1)
    output2=(functools.reduce(Add,output1))
    print(output2)


if __name__=="__main__":
    main()