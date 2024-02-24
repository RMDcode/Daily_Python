def Display(Name,Age,Marks):
    print("Name is :",Name)
    print("Age is :",Age)
    print("Marks is :",Marks)

def main():
    print(" Demonstration of keyword arguments")

    Display(Name="Amit",Age=25,Marks=89)
    Display(Marks=50,Name="Sagar",Age=50)

if __name__=="__main__":
    main()  