# Write a function to return True
# if the first and last number of a given list is same.
# If numbers are different then return False.

def check(number_list):
    print('Given List:', number_list)

    first_number = number_list[0]
    last_number = number_list [4]

    if first_number == last_number:
        return True
    else:
        return False

first_list = [10, 20, 30, 40, 10]
print('The result is:', check(first_list))

second_list = [75, 65, 35, 75, 30]
print('The result is:', check(second_list))