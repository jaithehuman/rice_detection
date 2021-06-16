dir = "./exp/test/"
f = open(dir+"result.txt","w+")
x = 5
f.write("Hello World!" + str(x))
# f.write(str(x))
f.close()