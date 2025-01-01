numbers = []
for i in range(5):
    a = int(input())
    numbers.append(a)

def find_max(numbers):
    max_num = numbers[0]
    for num  in numbers:
        if num > max_num:
            max_num = num
    return max_num
            

print(f"Maximum number: {find_max(numbers)}")