def check_numbers(nums):
    all_equal = True
    for i in range(1, len(nums)):
        if nums[i] != nums[0]:
            all_equal = False
            break

    if all_equal:
        return "Все числа равны"

    all_diff = True
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                all_diff = False
                break
        if not all_diff:
            break

    if all_diff:
        return "Все числа разные"

    return "Есть равные и неравные числа"

line = input().split()
numbers = []
for x in line:
    numbers.append(int(x))
print(check_numbers(numbers))
