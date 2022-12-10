# Vatsal Shah
# 10474245

import math

# Question 1
def twoMaxes(L):
    res0 = []
    res1 = []
    res = [res0, res1]
    if len(L) == 0:
        return res
    
    # row max
    for i in L:
        maxi = -math.inf
        res0.append(max(maxi, max(i)))
    
    # col max
    for i in range(len(L[0])):
        maxi = -math.inf
        for j in L:
            maxi = max(maxi, j[i])
        res1.append(maxi)
    return res
print("--> Question 1")
print(twoMaxes([[1, 2, 3], [11, 5, 6], [5, 8, 9]])) # [[3, 11, 9], [11, 8, 9]]
print(twoMaxes([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])) # [[3, 6, 9], [10, 11, 12]]
print(twoMaxes([[1, 2, 3]])) # [[3], [1, 2, 3]]


# Question 2
def dictionaryCollector(L):
    if len(L) == 0:
        return {}
    resDict = {'int': 0, 'string': ""}
    for i in L:
        if type(i) == int:
            resDict['int'] = resDict['int'] + i
        elif type(i) == str:
            resDict['string'] = resDict['string'] + i
            
    return resDict
print("--> Question 2")
print(dictionaryCollector([1, 2, 3, "a", "b", "c"]))
L = [True, 1, 4, 5, 'hello', 10, '10', 'world']
print(dictionaryCollector(L)) # {'int': 20, 'string': 'helloworld'}
print(dictionaryCollector([])) # {}
print(dictionaryCollector([1, 2, 3, 4, 5])) # {'int': 15, 'string': ''}
print(dictionaryCollector(['a', 'b', 'c', 'd', 'e'])) # {'int': 0, 'string': 'abcde'}


# Question 3
def selectionSort(L):
    for i in range(len(L)):
        minIndex = i
        for j in range(i, len(L)):
            if L[j] < L[minIndex]:
                minIndex = j
        L[i], L[minIndex] = L[minIndex], L[i]

print("--> Question 3")
L = [4,6,783,1,12,5,1]
x = selectionSort(L)
print(x) # None
print(L) # [1, 1, 4, 5, 6, 12, 783]

# Question 4
class Circle:
    def __init__(self, R):
        try:
            assert type(R) == int
            self.radius = R
        except AssertionError:
            print("Radius must be an integer")

    def __str__(self):
        return "Radius: " + str(self.radius)

    def area(self):
        return math.pi * math.pow(self.radius, 2)

class Sphere(Circle):
    def area(self):
        return 4 * math.pi * math.pow(self.radius, 2)
    
    def volume(self):
        return (4/3) * math.pi * math.pow(self.radius, 3)

print("--> Question 4")    
c = Circle(3)
print(c) # Radius: 3
print(c.area()) # 28.274333882308138
s = Sphere(4)
print(s) # Radius: 4
print(s.area()) # 201.06192982974676
print(s.volume()) # 268.082573106329


# Question 5
def preciseDivision(a,b):
    try:
        assert (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)
        return a/b

    except ZeroDivisionError:
        return float(math.inf)
    except:
        return None

print("--> Question 5")
print(preciseDivision(1,2)) # 0.5 
print(preciseDivision(1,0)) # inf
print(preciseDivision(1,4.0)) # 0.25
print(preciseDivision("D", "A")) # None

