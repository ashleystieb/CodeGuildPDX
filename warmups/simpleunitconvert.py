# create function that converts miles to feet
# 1 mile = 5280 feet

def miles_to_feet(miles):
    return miles * 5280

def main():
    user_input = float(input("Enter the number of miles to convert to feet: "))
    print(miles_to_feet(user_input))

main()
