##rotLeft function
##    input:  a list(a) of integers to rotate,
##            an integer(d) number of rotations to perform
##    output: the rotated list

a = [1,2,3,4,5]
d = 4

def rotLeft(a,d):
    a = a[d:] + a[:d]
    print(type(a))        
    print(a)
rotLeft(a,d)
