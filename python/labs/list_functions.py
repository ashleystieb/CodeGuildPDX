
# slices last number from list and returns it
def slice_last(num_list):
    '''
    >>> numbers = [1,2,3,4,5]
    >>> slice_last(numbers)
    5
    '''
    return num_list.pop(-1)

# returns list in reverse order
def reverse_list(num_list):
    '''
    >>> numbers = [1,2,3,4]
    >>> reverse_list(numbers)
    [4, 3, 2, 1]
    '''
    return num_list[::-1]

# doubles every other number on reversed list
def double_every_other(num_list):
    '''
    >>> numbers = [1,2,3,4]
    >>> double_every_other(numbers)
    [4, 6, 2, 2]
    '''
    num_list = num_list[::-1]
    for i in range(1,len(num_list),2):
        num_list[i] = num_list[i] * 2
    return num_list

# subtracts nine from numbers over nine on list
def subtract_from_digits(num_list):
    '''
    >>> numbers = [9,10,11,12]
    >>> subtract_from_digits(numbers)
    [9, 1, 2, 3]
    '''
    for i in range(0,len(num_list)):
        if num_list[i] > 9:
            num_list[i] = num_list[i] - 9
    return num_list

# adds up the sum of the values on the list
def sum_values(num_list):
    '''
    >>> numbers = [1,2,3,4]
    >>> sum_values(numbers)
    10
    '''
    sum = 0
    for i in num_list:
        sum = sum + i
    return sum

# calls each function
def main():
    numbers = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]
    print(slice_last(numbers))
    print(reverse_list(numbers))
    print(double_every_other(numbers))
    print(subtract_from_digits(numbers))
    print(sum_values(numbers))

main()

if __name__ == '__slice_last__':
    import doctest
