#input form the user
virusText = input("Enter a String :) : ")

#this function will create a file
with open(virusText, 'w') as f:
    file = f.write("this is a test file")


#loops thorugh

for i in range(1,10000000000000000000000000000000000000000000000000000):
#this is creating a new file
    a = open(virusText, "a")
    b = a.write("\n this will append to the output file ")
    a.close() 
    # print(i)

#this is reading from the file
f = open(virusText, "r")
d = f.read()
print(d,end="")
f.close()
