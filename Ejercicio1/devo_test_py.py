import math
import sys


# method to obtain the divisors of n
def getDivisors(n):
    divisors = []
    if n < 2:
        return divisors
    else:
        divisors.append(1)
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                if n / i == i:
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(int(n / i))
            i += 1
    return divisors


# method to obtain the category of n
def getCategory(n):
    divisors = getDivisors(n)
    suma = sum(divisors)

    if suma == n:
        return 'Perfecto'

    elif suma > n:
        return 'Abundante'

    return 'Defectivo'


# main with argument to run in command window
if __name__ == '__main__':
    num = int(sys.argv[1])
    cat = getCategory(num)
    print(cat)
