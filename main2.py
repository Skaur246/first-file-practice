from odd_even import check_odd_even

def check_odd_even(numbers):
    for num in numbers:
        result = "even" if num % 2 == 0 else "odd"
        print(f"{num} is {result}.")


