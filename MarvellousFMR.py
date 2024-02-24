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
