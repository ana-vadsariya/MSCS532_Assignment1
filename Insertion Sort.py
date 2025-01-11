def insertion_sort(array):
    for i in range(0,len(array)):
        temp = array[i]
        for j in range(i-1, -1,-1):
            if temp > array[j]:
                array[j+1] = array[j]
                array[j] = temp
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

array = [1, 12, 3, 44, 5, 6]
insertion_sort(array)
