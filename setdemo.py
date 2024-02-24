print("Demonstration of Set")

set1={11,78.89,"hello",True}
print(set1)

#print(set1[1])

for i in set1:
    print(i)

set2={11,78,11,89,78}
print(set2)

set2.add(101)
print(set2)

set2.remove(101)
print(set2)

print("enter the value that you want to search in set:",end="")
no=int(input())

for value in set2:
    if(no==value):
        print("Element is present")
        break