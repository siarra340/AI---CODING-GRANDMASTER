def create_fibonacci(n):
    series = []
    num1, num2 = 0,1

    for _ in range(n):
        series.append(num1)
        num1, num2 = num2, num1 + num2

    return series

term = int(input("Enter the number of terms: "))

if term <= 0:
    print("Enter a postive integer")
else:
    ans = create_fibonacci(term)

    print(f"The Fibonacci sequence up to {term} terms: ")
    print(ans)