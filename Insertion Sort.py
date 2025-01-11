#Insertion Sort Algorithm which sorts the array in decreasing order

def insertion_sort(array):
    #Outer loop which will keep track of the temp var
    for i in range(0,len(array)):
        temp = array[i]
        #Inner loop which will compare temp value with all the values on the left
        #if temp value is greater it will swap with the one on left
        for j in range(i-1, -1,-1):
            if temp > array[j]:
                array[j+1] = array[j]
                array[j] = temp
    print("Sorted Array")    
    #print the sorted array by calling print_array function            
    print_array(array)

def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

#Provided array to be sorted
array = [1, 12, 3, 44, 5, 6]

#print before sorting
print("Given Array")  
print_array(array)

#perform the sorting
insertion_sort(array)
