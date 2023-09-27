numInputs = int(input('Enter number of numbers'))

if(numInputs<2):

    print("Need atleast 2 numbers")

    exit()

 

maxNum = int(input("Enter Number: "))

maxNum2 = int(input("Enter Number: "))

 

if(maxNum2>maxNum):

    temp = maxNum2

    maxNum2 = maxNum

    maxNum = temp

 

for x in range(2,numInputs):

    num = int(input("Enter Number: "))

    if(num>maxNum):

        maxNum2 = maxNum

        maxNum=num

    if(num>maxNum2 and num<maxNum):

        maxNum2 = num


    if(maxNum==maxNum2):
        print('No largest element is present')

    else:
     print(maxNum2)


