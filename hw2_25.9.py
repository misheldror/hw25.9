
numbers: list[int] = []

while True:
    number: int = int(input("Enter a number: "))
    if 0 <= number <= 10:
        numbers.append(number)
        count: int = numbers.count(number)
        if count > 0:
            print(f"statistics[{number}] : {count}")
    if number == -999:
        break
    numbers.count(number)