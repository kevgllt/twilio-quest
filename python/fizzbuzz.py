# Create a program that accepts any number of command line arguments. The arguments will be whole/integer numbers. Your script will need to examine all these numbers and execute the following conditional logic:

# If the number is divisible by 3, print the text: fizz
# If the number is divisible by 5, print the text: buzz
# If the number is divisible by both 3 and 5, print the text: fizzbuzz
# If none of the above are true, print the number


import sys

inputs = sys.argv
inputs.pop(0)

#inputs = ['1','3','6','2']

#print(f"not int {inputs}\n")

def convert_int(num):
    item = []
    for items in num:
       item.append(int(items))
    return item

#print(convert_int(inputs))

inputs_int = convert_int(inputs)

# print(f"int convert ok {inputs_int}\n")

def have_three(num):
    for items in num:
        if items % 3 == 0 and items % 5 == 0:
            print(f"fizzbuzz")
        elif items % 3 == 0:
            print(f"fizz")
        elif items % 5 == 0:
            print(f"buzz")
        else:
            print(f"{items}")

print(have_three(inputs_int))


