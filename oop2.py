class demo:
    def __init__(self,value1,value2):       #constructors
        print("Inside init method")
        self.No1=value1
        self.No2=value2


    def display(self):
        print("Value of No1 :",self.No1)
        print("Value of No2 :",self.No2)

def main():
    print("Demonstration of object orientation")

    obj1=demo(10,20)          #object1 #__init__(100,10,20)
    obj2=demo(11,21)          #object2 #__init__(200,11,21)

    obj1.display()  #display(100)
    obj2.display()  #display(200)


if __name__=="__main__":
    main()