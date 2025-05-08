try:
    input = input().split(",")
    nums = [int(num) for num in input]
except ValueError:
    print("некорректные данные: введите числа через запятую")
except Exception as e:
    print(f"Ошибка: {e}")

input = input().split(", ")
nums = [int(num) for num in input]

even_numbers = [x for x in nums if x % 2 == 0]

max_num, min_num = max(nums), min(nums)

n = len(nums)
for i in range(n):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(f"Четные числа: {even_numbers}")
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
print(f"Отсортированный список: {nums}")
