# Vatsal Shah

def dot(L,K):
    if len(L) != len(K):
        return float('-inf')
    if not L and not K:
        return 0
    elif not L or not K:
        return float('-inf')
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])

print(dot([5, 3], [6, 4]))

def explode(S):
    if not S:
        return []
    else:
        return [S[0]] + explode(S[1:])

print(explode('spam'))
print(explode('   '))

def runningAverage(L):
    sum = 0
    for i, j in enumerate(L):
        sum += j
        L[i] = sum/(i+1)
    return L

print(runningAverage([1,2,3,4,5]))
print(runningAverage([]))


def double(n):
    return 2 * n

def isEven(n):
    return n % 2 == 0

def customMap(func, L):
    if not L:
        return []
    else:
        return [func(L[0])] + customMap(func, L[1:])

def customFilter(func, L):
    if not L:
        return []
    else:
        if func(L[0]):
            return [L[0]] + customFilter(func, L[1:])
        else:
            return customFilter(func, L[1:])


print(customMap(double, [1,2,3,4,5]))
print(customFilter(isEven, [1,2,3,4,5]))