#Program to Print Math Table of A Number
sample_number = int(input("Enter a number to print its math table: "))
print(f"Table of {sample_number}:\n")
for i in range(1,11):
    print('%02d*%02d=%03d'%(sample_number,i,sample_number*i))