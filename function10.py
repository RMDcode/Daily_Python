def Add(A,B):
    return A+B

sub=lambda A,B:A-B

#Function accepts parameters as another functiom
def Marvellous(FPTR):
    print(type(FPTR))
    print(FPTR)
    Ans=FPTR(11,7)  #Call function here
    print("Addition is :",Ans)
    print("Substraction is :",Ans)

def main():
    Marvellous(Add)     #0x00000186B08F04A0
    Marvellous(sub)     #0x00000186B0AB8CC0

if __name__=="__main__":
    main()