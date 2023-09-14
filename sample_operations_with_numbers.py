def adding(num_1, num_2):
    result_a = num_1 + num_2
    return result_a


def subtracting(num_1, num_2):
    result_s = num_1 - num_2
    return result_s


def multiplying(num_1, num_2):
    result_m = num_1 * num_2
    return result_m


def dividing(num_1, num_2):
    result_d = num_1 / num_2
    return result_d


def power(num_1, num_2):
    result_p = pow(num_1, num_2)
    return result_p


number_1 = float(input("Write a number 1: "))
number_2 = float(input("Write a number 2: "))

print("Select the operation on the numbers and enter the corresponding sign into the console")
print(' 1) Add +\n 2) Subtract -\n 3) Multiply *\n 4) Divide /\n 5) Raise to a power **\n')

operation = str(input("Write an operation: "))
if operation == '+':
    result = adding(number_1, number_2)
    print(result)
elif operation == '-':
    result = subtracting(number_1, number_2)
    print(result)
elif operation == '*':
    result = multiplying(number_1, number_2)
    print(result)
elif operation == '/':
    result = dividing(number_1, number_2)
    print(result)
elif operation == '**':
    result = power(number_1, number_2)
    print(result)
else:
    print("Error, you have to choose an operation")
