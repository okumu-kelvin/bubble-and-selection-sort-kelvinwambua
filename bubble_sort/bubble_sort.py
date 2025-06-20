def bubble_sort(unsorted_list):
    for i  in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[i]:
                unsorted_list[j], unsorted_list[i]= unsorted_list[i], unsorted_list[j]
    return unsorted_list

    
