add= lambda A,B:A+B

sub=lambda A,B:A-B

#Function accepts multiple parameters and call another function from it and return multiple variable
def Marvellous(value1,value2):
    Ans1=add(value1,value2)
    print("Addition is :",Ans1)
    Ans2=sub(value1,value2)
    print("Substraction is :",Ans2)
    
    return Ans1,Ans2

def main():
    Arr=Marvellous(11,7)
    print("Addition is :",Arr[0])
    print("Substraction is :",Arr[1])

    
if __name__=="__main__":
    main()