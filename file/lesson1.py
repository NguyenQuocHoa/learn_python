path = "D:\\learn_python\\file\\demo.txt"
# read file content
f = open(path, "r")
print("====================> BEFORE WRITE <====================")
for line in f:
    print(line)
f.close()

# append file content
f = open(path, "a")
f.write("\nThis is new content line")
f.close()

# check result after write
print("====================> AFTER WRITE <====================")
f = open(path, "r")
for line in f:
    print(line)
f.close()