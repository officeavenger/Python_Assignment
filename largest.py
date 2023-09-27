n= int(input("Enter the total count of numbers"))

max=float('-inf')
for i in range(0,n):
    ele=int(input("Enter element"))
    if(ele>max):
        max=ele

print(max)
      