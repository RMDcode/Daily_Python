def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

#Function accepts multiple parameters and call another function from it
def Marvellous(value1,value2):
    Ans=Add(value1,value2)
    print("Addition is :",Ans)
    Ans=Sub(value1,value2)
    print("Substraction is :",Ans)
    

def main():
    Marvellous(11,7)
    
if __name__=="__main__":
    main()