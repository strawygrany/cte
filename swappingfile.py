
sample1="this is sample 1"
sample2="ths is sample2"

data_a = sample2
data_b = sample1
def swapFileData():
    with open(sample1, "r"):
     data_a=sample1.read()

    with open(sample2,"r"):
     data_b=sample2.read()

    with open(sample1, "w"):
     sample2.write(data_b)
    
    with open(sample2, "w"):
     sample1.write(data_a)

print(data_a)
print(data_b)