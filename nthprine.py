n = int(input())
cnt = 0

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1000):
    if isPrime(i):
        cnt += 1
    if cnt == n:
        print(i)
        break