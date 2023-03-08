def binary_search():
    target = 100
    list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    left = 0
    right = len(list) - 1
    index = -1
    while left <= right:
        middle = int((left + right)/2)
        if list[middle] == target:
            index = middle + 1
            break
        if list[middle] > target:
            right = middle
        if list[middle] < target:
            left = middle + 1
    print(index)


binary_search()
