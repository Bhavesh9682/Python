def sample(n):
    s = 0
    i = 0
    while n > 0:
        r = n % 10
        p = 8 ** i
        s = s + p * r
        i=i+1
        n=n//10  # Use integer division to get the next digit
    return s

N = int(input("Enter a number: "))
result=sample(N)
print("The value of s is",result)
