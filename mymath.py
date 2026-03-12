class MyMath:
    def calculate(self, operation, n):
        if operation.lower() == "sum":
            result = n * (n + 1) // 2
            print(f"Sum of first {n} natural numbers: {result}")

        elif operation.lower() == "prime":
            primes = []
            num = 2
            while len(primes) < n:
                for i in range(2, int(num**0.5)+1):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
                num += 1
            print(f"First {n} prime numbers: {primes}")

        elif operation.lower() == "fibonacci":
            fib = []
            a, b = 0, 1
            for _ in range(n):
                fib.append(a)
                a, b = b, a + b
            print(f"Fibonacci series of {n} numbers: {fib}")

        elif operation.lower() == "factorial":
            factorial = 1
            for i in range(1, n+1):
                factorial *= i
            print(f"Factorial of {n}: {factorial}")

        else:
            print("Invalid operation! Choose: sum, prime, fibonacci, factorial.")


# Example usage
math_tool = MyMath()

print("Welcome to the Mathematical Utility Tool")
print("Operations: sum, prime, fibonacci, factorial")
operation = input("Enter the operation: ")
n = int(input("Enter the value of n: "))

math_tool.calculate(operation, n)