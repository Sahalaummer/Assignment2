def print_odd_numbers(li):
    odd_numbers = [num for num in li if num % 2 != 0]
    print("Odd numbers in the list:", odd_numbers)

my_list = [45, 78, 4, 34, 56, 101, 9]
print_odd_numbers(my_list)
