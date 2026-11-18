while True:
    print("\n----- MENU -----")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter a number: "))
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            print(n, "is a Prime number")
        else:
            print(n, "is not a Prime number")

    elif choice == 2:
        n = int(input("Enter a number: "))
        original = n
        reverse = 0

        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10

        if original == reverse:
            print(original, "is a Palindrome")
        else:
            print(original, "is not a Palindrome")

    elif choice == 3:
        n = int(input("Enter a number: "))
        original = n
        digits = len(str(n))
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit ** digits
            n = n // 10

        if total == original:
            print(original, "is an Armstrong number")
        else:
            print(original, "is not an Armstrong number")

    elif choice == 4:
        n = int(input("Enter a number: "))
        factorial = 1

        for i in range(1, n + 1):
            factorial = factorial * i

        print("Factorial =", factorial)

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        print("Fibonacci Series:")

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()

    elif choice == 6:
        print("Program exited.")
        break

    else:
        print("Invalid choice! Please try again.")