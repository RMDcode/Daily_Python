
#Function defines another function inside it and return as its return value
def Demo(value1,value2):         #0X200
    def Add(A,B):   #0X100
        return A+B

    return Add(value1,value2)      #return 0X100

def main():         #0X300  
    ret=Demo(10,7)      #0X200()
    
    print("Addition is :",ret)


if __name__=="__main__":
    main()          #0X300()