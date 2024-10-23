# def printPowerSize(set, set_size):
#     power_set_size= 2**set_size
#     outer=0
#     inner=0
#     for outer in range(0,power_set_size):
#         for inner in range(0,set_size):
#             if((outer& (1<<inner))>0):
#                 print(set[inner], end="")
#         print("")

# size=int(input("enter your array size"))
# set=[]
# for i in range(0,size):
#     n=int(input("enter element"))
#     set.append(n)
# printPowerSize(set,len(size))

def flips(num1,num2):
    flip=0
    while (num1 > 0 or num2 > 0):
        t1= num1 & 1
        t2= num2 & 1
        if t1 !=t2:
            flip+=1
        num1>>=1
        num2>>=1
    return flip
num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("numbers of flips needed",flips(num1, num2))
