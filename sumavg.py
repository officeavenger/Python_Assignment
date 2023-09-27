def sum(*args):
    sum=0
    for value in args:
        sum+=value
    return sum
    


def average(*args):
    avg=sum(args)/len(args)
    return avg


average(1,2,3,4)