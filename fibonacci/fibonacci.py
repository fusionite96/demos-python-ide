# Python program to calculate the Fibonacci sequence
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55

# Add a comment
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))



# Calculate Fibonacci
result = fibo(10)
print('fibo(10) = ' + str(result))
