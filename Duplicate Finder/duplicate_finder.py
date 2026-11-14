def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    if duplicates:
        print("Duplicate elements:", sorted(duplicates))
    else:
        print("No duplicates found!")


print("DUPLICATE FINDER")
values = input("Enter numbers separated by spaces: ")
numbers = values.split()
find_duplicates(numbers)
