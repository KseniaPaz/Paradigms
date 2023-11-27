# Задача 1.
# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для сортировки чисел
# в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Для убывающего порядка используется <
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return numbers

numbers = [64, 25, 12, 22, 11]
bubble_sort(numbers)
print("Отсортированный список (императивно):", numbers)