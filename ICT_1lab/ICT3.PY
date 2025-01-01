num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    for _ in range(num_terms):
        print(a)
        a, b = b, a + b
