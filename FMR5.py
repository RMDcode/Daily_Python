import functools

CheckEven = lambda No:(No % 2 ==0)
        
Increase= lambda No : No+2

Add= lambda A,B: A+B


def main():
    Data=[]
    print("Enter number of elements :")
    size=int(input())
    
    
    print("Enter the elements:")
    for i in range(size):
        value=int(input())
        Data.append(value)

    output=list(filter(CheckEven,Data))
    print("Output after filter :",output)
    output1=list(map(Increase,output))
    print("Output after Map :",output1)
    output2=(functools.reduce(Add,output1))
    print("Output after reduce :",output2)


if __name__=="__main__":
    main()