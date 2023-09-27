start = int(input('Enter start num'))

end = int(input('Enter end num'))

 

def check_prime(num):

    isPrime = True

    for x in range(2,num//2):

        if(num%x==0):

            isPrime=False

            break

    return isPrime

 

for x in range(start,end):

    if(check_prime(x)):

        print(x)
