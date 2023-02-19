import sys

def adiction(first_number, second_number):
    result_sum = int(first_number) + int(second_number)
    return result_sum

sum_to_use = adiction(sys.argv[1], sys.argv[2])

if sum_to_use == 0 or sum_to_use <= 0:
    print("You have chosen the path of destitution.")
elif sum_to_use >= 1 and sum_to_use <= 100:
    print("You have chosen the path of plenty.")
else:
    print("You have chosen the path of excess.")
