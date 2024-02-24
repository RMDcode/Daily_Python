def Display(*Values):
    print(type(Values))
    print(len(Values))
    print(Values)

def main():
    print(" Demonstration of Default arguments")
    Display(10,20,30,40,50)



if __name__=="__main__":
    main()  