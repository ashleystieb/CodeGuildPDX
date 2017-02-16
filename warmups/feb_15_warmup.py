def how_many(num_list, number):
    '''
    >>> num_list = [1,1,1,1,1,1]
    >>> how_many(num_list,1)
    6
    >>> second_num_list = [1,4,3,7,7,8,9]
    >>> how_many(second_num_list,7)
    2
    >>> how_many(second_num_list,20)
    0
    '''
    times = 0
    for num in num_list:
        if num == number:
            times += 1
    return times
