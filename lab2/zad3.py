import random

def f_3n(n):
    a = 0
    for i in range(n):
        a += i
    for i in range(n):
        a += i
    for i in range(n):
        a += i


def f_nlongn(n):

    def quicksort(nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
            s_nums = []
            m_nums = []
            e_nums = []
            for n in nums:
                if n < q:
                    s_nums.append(n)
                elif n > q:
                    m_nums.append(n)
                else:
                    e_nums.append(n)
            return quicksort(s_nums) + e_nums + quicksort(m_nums)

    a = [random.randint(1, 100) for x in range(n)]
    return quicksort(a)


def f_nfactorial(n):
    s = 0
    if n <= 1:
        return 1
    for i in range(n):
        s += f_nfactorial(n - 1)
    return s


def f_nst3(n):
    a = []
    for i in range(n):
        for j in range(n):
            for z in range(n):
                a.append((i, j, z))


def f_3nlogn(n):
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

    a = [i for i in range(n)]
    x1, x2, x3 = map(int, input().split())
    binary_search(a, x1)
    binary_search(a, x2)
    binary_search(a, x3)

