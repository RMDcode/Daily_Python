def Addition(No1,No2):
    Result = 0
    Result = No1+No2
    return Result


def main():
    value1=int(input("Enter First Number : "))
    value2=int(input("Enter Second number : "))

    Answer = 0
    Answer = Addition(value1,value2)

    print("Addition is : ",Answer)

if __name__=="__main__":           #starter

    main()