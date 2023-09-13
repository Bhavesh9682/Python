def fibonacci_series(n):
    fib_series = [0, 1]  # Initial values of the Fibonacci series

    while len(fib_series) < n:
        next_fib = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        fib_series.append(next_fib)

    return fib_series

# Input the number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci series
fibonacci = fibonacci_series(num_terms)
print("Fibonacci Series:", fibonacci)
