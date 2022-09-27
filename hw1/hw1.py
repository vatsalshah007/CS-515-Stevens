def cToF(temp):
    return (temp * (9/5)) + 32

def fToC(temp):
    return (temp - 32) * (5/9)

def shortStrings(L, n):
    shortString = list(filter(lambda x: (len(x) <= n), L))
    return shortString

def doubleStrings(L):
    def doubleFunc(myString):
        return myString + myString
    double = list(map(doubleFunc, L))
    return double

def pigLatin(s):
    pigLatStr = s[1:] + s[0] + "ay"
    x = list(filter(lambda i: (i in pigLatStr), pigLatStr))
    return x

print(cToF(0))
print(fToC(10))
print(shortStrings(["a", "b", "aa"], 1))
print(doubleStrings(["a", "cc"]))
print(pigLatin("hello"))

# Bonus
def stringBalance(s):
    countFH = 0
    countLH = 0
    s = s.lower()
    for i in s:
        if ord(i) <= 109:
            countFH = countFH +1
        else:
            countLH = countLH + 1
    if countFH == countLH:
        return 0
    elif countFH > countLH:
        return -2
    else:
        return 3

print(stringBalance("azazazaz"))