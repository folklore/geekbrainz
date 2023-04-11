def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l
    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r
    # Заменяем корень, если нужно
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)


# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Свап 

        heapify(arr, i, 0)


arr = [12, 11, 3, 13, 5, 2, 11, 6, 10, 7]
heapSort(arr)

n = len(arr)
print ("Sorted array is")
for i in range(n):
    print("%d" % arr[i])


# sg@mbp ads % python3 2.py 
# Sorted array is
# 2
# 3
# 5
# 6
# 7
# 10
# 11
# 11
# 12
# 13
# sg@mbp ads %
