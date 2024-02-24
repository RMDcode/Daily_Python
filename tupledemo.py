print("Demonstration of tuple")

tuple1=(11,"hello",90.89,False)
print(tuple1)

print(type(tuple1))
print(len(tuple1))

print(tuple1[1])

#tuple1[0]=12           #NA
#print(tuple1)

#tuple1.append(67)
#print(tuple1)

tuple2=(11,89,11,67,11)
print(tuple2)

for value in tuple2:
    print(value)

for i in range(len(tuple2)):
    print(tuple2[i])