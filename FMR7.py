import functools

#CheckEven =         
#Increase= 
#Add= 

def main():
    Data=[]
    print("Enter number of elements :")
    size=int(input())
    
    
    print("Enter the elements:")
    for i in range(size):
        value=int(input())
        Data.append(value)

    output=list(filter(lambda No:(No % 2 ==0),Data))
    print("Output after filter :",output)
    output1=list(map(lambda No : No+2,output))
    print("Output after Map :",output1)
    output2=(functools.reduce(lambda A,B: A+B,output1))
    print("Output after reduce :",output2)

    print(functools.reduce(lambda A,B: A+B,map(lambda No : No+2,filter(lambda No:(No % 2 ==0),Data))))

if __name__=="__main__":
    main()