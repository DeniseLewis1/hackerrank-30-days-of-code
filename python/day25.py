# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return "Not prime"
        return "Prime"
    return "Not prime"
    
T = int(input())
for n in range(T):
    num = int(input())
    print(is_prime(num))