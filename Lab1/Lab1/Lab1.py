from datetime import date, datetime

# Euclidean division algorithm
def gcd1(a, b):
    reminder = b

    while(reminder != 0):
        reminder = a % b
        a = b
        b = reminder

    return a

#Substraction algorithm
def gcd2(a, b):
    if (a == 0):
        return b;

    if (b == 0):
        return a;
    
    while(a != b):
        if (a > b):
            a = a - b
        else: 
            b = b - a

    return a 

# Get gcd by multipling with the prime divisors
def gcd3(a, b):
    i = 2
    currentLcm = 1

    if (a == 0 or b == 0):
        currentLcm = max(a, b)
    
    div = 2

    while(a != 1 and b != 1 and i <= a and i <= b):
        nrA = 0
        nrB = 0

        while (a % div == 0):
            nrA += 1
            currentLcm *= div
            a //= div

        while (b % div == 0):
            nrB += 1
            b //= div

        while (nrB < nrA):
            currentLcm //= div
            nrA -= 1

        div += 1

    return currentLcm

#test function for "normal" sized numbers, under 20 digits
def testFunction(gcd):
    testValuesNormal = [[0, 24], [12, 14], [2115, 13125], [87832455, 783764940], [15354864641, 3597837933979], [33333333, 9999999900000], [339999333111222, 9999999997554], [713724152, 241693984], [99555222, 2220055599]]
    testValuesAverageSize = [[12, 24], [12, 14], [2115, 13125], [23423, 589099], [15354864641, 3597837933979], [33333333339999333111222, 999999999999999992220]]

    startTime = datetime.now()

    for pair in testValuesNormal:
        if(gcd == gcd1):
            print("Euclidean division algorithm")
        if(gcd == gcd2):
            print("Substraction algorithm")
        if(gcd == gcd3):
            print("Commomn divisors algorithm")
        print('(', pair[0], ', ', pair[1], ') = ', gcd(pair[0], pair[1]))

    endTime = datetime.now()

    return endTime - startTime

#test function, for average sized numbers
def testFunctionBigNumbers(gcd):
    testValuesAverageSize = [[123456789123456789000, 987654321987654321330], [3321333421234123413412412413, 6642666842468246826824824826], [33333333339999333111222, 999999999999999992220]]

    startTime = datetime.now()

    for pair in testValuesAverageSize:
        print('(', pair[0], ', ', pair[1], ') = ', gcd(pair[0], pair[1]))

    endTime = datetime.now()

    return endTime - startTime

print("time: ", testFunction(gcd1), "\n") # time -> 0:00:00.000992
print("time: ", testFunction(gcd2), "\n") # time -> 0:00:00.263296
print("time: ", testFunction(gcd3), "\n") # time -> 0:00:01.835780
print("average size numbers: ")
print("time: ", testFunctionBigNumbers(gcd1)) 