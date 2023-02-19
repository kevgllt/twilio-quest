import sys

first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

result_sum = first_number + second_number
result_difference = first_number - second_number
result_product = first_number * second_number
result_quotient = first_number / second_number

print(f"Sum result is: {result_sum}")
print(f"Difference result is: {result_difference}")
print(f"Product result is: {result_product}")
print(f"quotient result is: {result_quotient}")
