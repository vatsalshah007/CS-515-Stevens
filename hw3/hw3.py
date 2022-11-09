# Vatsal Shah

# Question 1
import traceback
import sys

def sprial(L):
        result = []
        m = len(L)
        n = len(L[0])
        left = 0
        top = 0
        right = n-1
        bottom = m-1
        while(len(result) < m*n):
            # left to right ➡️
            for column in range(left, right+1):
                result.append(L[top][column])

            # top to bottom ⬇️
            for row in range(top+1, bottom+1):
                result.append(L[row][right])
            
            # check if we are in different row
            if top != bottom:
                # right to left ⬅️
                for col in range(right-1, left-1, -1):
                    result.append(L[bottom][col])
                
            # check if we are in differet column
            if left != right:
                # bottom to top ⬆️
                for row in range(bottom - 1, top, -1):
                    result.append(L[row][left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return result
# Time Complexity: O(m*n)
print(sprial([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# Question 2
def inverter(D):
    res= {}
    for i in D:
        if D[i] not in res:
            res[D[i]] = i
        else:
            if type(res[D[i]]) == list:
                res[D[i]].append(i)
            else:
                res[D[i]] = [res[D[i]], i]
    return res
# Time Complexity: O(n)
print(inverter({1: 10, 2: 20, 3: 30, 4: 30}))

# Question 3
def matrixMultiply(A,B):
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    # try:
    if len(A[0]) != len(B):
        raise ArithmeticError("Invalid Matrix Dimensions")
    # except ArithmeticError:
    #     print(ArithmeticError, ": ", sys.exc_info()[1])
    #     traceback.print_exception(*sys.exc_info())
    #     exit(0)
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result
# Time Complexity: O(m*n*k)
print(matrixMultiply([[1,2,3],[4,5,6]], [[1,2],[3,4]]))

# Question 4
def twoSum(L,t):
    indexDict = {}
    res = []
    for i, j in enumerate(L):
        if t-j in indexDict:
            res.append([indexDict[t-j], j])
        indexDict[j] = i
    return res
# Time Complexity: O(n)
print(twoSum([3,5,2,-4,8,11], 7))
