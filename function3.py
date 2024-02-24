#Function accepts one or more parameter and return nothing
def Marvellous(Name,Age,city):
    print("Inside Marvellos Fucntion")
    print("Welcome :"+Name)
    print("Your age is :",Age)
    print("Your city is :",city)

def main():
    Marvellous("Amit",28,"Pune")
    Marvellous(Name="Sagar",Age=25,city="pune")    
   

if __name__=="__main__":
    main()