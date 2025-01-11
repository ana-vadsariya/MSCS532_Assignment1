def insertion_sort(array):
    for i in range(1,len(array)):
        temp = array[i]
        print("temp", temp)
        for j in range(i-1, 0,-1):
            print("j", array[j])
            if temp > array[j]:
                array[j+1] = array[j]
                array[j + 1] = temp
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

array = [12, 11, 13, 5, 6]
insertion_sort(array)
