##
##input:  s, string, to be repeated and counted
##        n, integer, length of string
##output: integer, number of times 'a' in string input that is (n) length
##
s = 'aba'
n = 10
def repeatedString(s,n):
    multiString = s*n
    total = multiString[:n].count('a')
    return total
print(repeatedString(s,n))
