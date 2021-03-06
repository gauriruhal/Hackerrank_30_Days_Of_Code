import os

# Complete the factorial function below.
def factorial(N):
    '''Function to calculate the factorial'''
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    RESULT = factorial(N)

    fptr.write(str(RESULT) + '\n')

    fptr.close()