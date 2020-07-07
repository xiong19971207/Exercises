def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

    return n


_list = [8, 6, 9, 1, 4, 2, 5]
print(bubble_sort(_list))
