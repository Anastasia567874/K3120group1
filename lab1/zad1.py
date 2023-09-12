def binary_search(sort_array: list, n: int):
    left = 0
    count = 0
    right = len(sort_array) - 1
    while left <= right:
        middle = (right + left) // 2
        if n == sort_array[middle]:
            return count
        elif n > sort_array[middle]:
            left = middle + 1
            count += 1
        else:
            right = middle - 1
            count += 1
    return 'ERROR'

n = int(input())
A = [int(x) for x in input().split()]
A.sort()
print(f'Для поиска данного числа потребуется шагов: {binary_search(A, n)}')