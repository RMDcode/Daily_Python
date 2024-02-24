#Function accepts parameter and return parameter
def Marvellous(value1,value2):
    if(value1>value2):
        return value1
    else:
        return value2

def main():
    ret=Marvellous(78,45)
    print("largest number is:",ret)

    ret=Marvellous(34,99)
    print("largest number is:",ret)


if __name__=="__main__":
    main()