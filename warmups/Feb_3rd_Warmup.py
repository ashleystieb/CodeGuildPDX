def print_numbers(number):
    for i in range(1,number + 1):
        if i % 2 == 0 and i % 3 == 0:
            print("Penguin")
        else:
            print(i)


print_numbers(20)
