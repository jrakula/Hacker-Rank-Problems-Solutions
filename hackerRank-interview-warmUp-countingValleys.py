##input:  int -> number of steps
##        string -> describing path with either (up) U or (down) D
##output: int -> number of times walked below 2 units deep. 
##def countingValleys(steps,path):
##
##    return(steps,path)
##
##
integer = 7
string = 'DDUUUDD'
##

def countingValleys(n, steps):
    seaLevel = valley = 0

    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if step == 'U' and seaLevel == 0:
            valley += 1
    
    return valley
print(countingValleys(integer, string))
