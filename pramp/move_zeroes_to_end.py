def moveZerosToEnd(array):
    write = 0
    for read in range(len(array)):
        if array[read] != 0:
            if array[write] == 0:
                array[read], array[write] = array[write], array[read]
            write += 1
    return array
