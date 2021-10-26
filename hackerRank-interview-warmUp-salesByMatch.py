##input:  ar = list of numbers
##        n = count of numbers in list
##output: count of distinct pairs in given list

def sockMerchant(n, ar):
    count = 0
    i = 0
    ar.sort()
    while i < n - 1:
        if ar[i] == ar[i+1]:
            count += 1
            i += 2
        else: 
            i += 1
    return count
