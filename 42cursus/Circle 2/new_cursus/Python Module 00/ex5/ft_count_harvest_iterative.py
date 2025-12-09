def ft_count_harvest_iterative():
    days = input("Days until harvest: ")

    for i in range(1, int(days) + 1):
        print("Day", int(i))
    print("Harvest time!")
