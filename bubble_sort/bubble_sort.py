def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        switched  =  False
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                switched = True
        if not switched:
            break
    return unsorted_list
    

