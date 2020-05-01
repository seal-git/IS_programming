def quick_sort (a, left_index , right_index):
    if left_index >= right_index:
        return

    print(A)
    pivot = a[(right_index + left_index ) // 2]
    i = left_index
    j = right_index

    while i <= j:
        while a[i ] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i ], a[j] = a[j],  a[i]
            i += 1
            j -= 1

    left = quick_sort (a , left_index , j)
    right = quick_sort (a , i , right_index )
    return

A = [15, 41, 5, 35, 18, 25, 8 ,9, 31, 3, 41]
quick_sort(A, 0 ,10)
print("sorted:")
print(A)

"""
[15, 41, 5, 35, 18, 25, 8, 9, 31, 3, 41]
[15, 3, 5, 9, 18, 8, 25, 35, 31, 41, 41]
[5, 3, 15, 9, 18, 8, 25, 35, 31, 41, 41]
[3, 5, 15, 9, 18, 8, 25, 35, 31, 41, 41]
[3, 5, 8, 9, 18, 15, 25, 35, 31, 41, 41]
[3, 5, 8, 9, 15, 18, 25, 35, 31, 41, 41]
[3, 5, 8, 9, 15, 18, 25, 31, 35, 41, 41]
[3, 5, 8, 9, 15, 18, 25, 31, 35, 41, 41]
[3, 5, 8, 9, 15, 18, 25, 31, 35, 41, 41]
sorted:
[3, 5, 8, 9, 15, 18, 25, 31, 35, 41, 41]
"""