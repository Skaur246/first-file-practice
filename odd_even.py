def check_odd_even(numbers):
    for num in numbers:
        
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

# Check for odd or even numbers in list 1
numbers1 = [10, 15, 22, 29, 30]
numbers2 = [1, 4, 7, 9, 12]
numbers3 = [100, 150, 200]
check_odd_even(numbers1)
check_odd_even(numbers2)
check_odd_even(numbers3)