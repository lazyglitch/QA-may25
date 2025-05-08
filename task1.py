try:

    input_str = input().split(",")
    nums = []
    for num_str in input_str:
        num_str = num_str.strip()

        # Проверка на whitespace
        if not num_str:
            raise ValueError("Empty string")

        # Проверка на нули
        if len(num_str) > 1 and (num_str.startswith("0") or num_str.startswith("-0")):
            raise ValueError("Leading zeros")

        # Конвертация в число
        try:
            num = int(num_str)
        except ValueError:
            raise ValueError(f"Invalid input: {num_str}")

        nums.append(num)

    even_numbers = [x for x in nums if x % 2 == 0]

    # сортировка
    n = len(nums)
    sorted_nums = nums.copy()
    for i in range(n):
        for j in range(n - i - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]

    print(f"Четные числа: {even_numbers}")
    print(f"Максимальное число: {max(nums)}")
    print(f"Минимальное число: {min(nums)}")
    print(f"Отсортированный список: {sorted_nums}")

except Exception as e:
    print(f"Error detected: {e}")
