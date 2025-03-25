def add_many_numbers(numbers) -> int:

    total = 0
    
    for number in numbers:
        total_so_far += number
        
    return total_so_far

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum_of_number = add_many_numbers(numbers)
    print("The sum of the numbers is:", sum_of_number)

if __name__ == "__main__":
    main()