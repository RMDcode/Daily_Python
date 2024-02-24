
CheckEven = lambda No:(No % 2 ==0)
Increase= lambda No : No+2
Add= lambda A,B: A+B

#Task:Name of function
#Elements: List of data elements
def filterX(Task,Elements):
    Result=[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret=Task(no)
        Result.append(Ret)
    return Result

def reduceX(Task,Elements):
    sum=0
    for no in Elements:
        sum=Task(sum,no)
    return sum

def main():
    Data=[]
    print("Enter number of elements :")
    size=int(input())
    
    
    print("Enter the elements:")
    for i in range(size):
        value=int(input())
        Data.append(value)

    output=list(filterX(CheckEven,Data))
    print("Output after filter :",output)
    output1=list(mapX(Increase,output))
    print("Output after Map :",output1)
    output2=(reduceX(Add,output1))
    print("Output after reduce :",output2)


if __name__=="__main__":
    main()