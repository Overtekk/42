def ft_count_harvest_recursive(days=None, current_day=1):
    if days is None:
        days = int(input("Days until harvest: "))
    else:
        for n in range(ft_count_harvest_recursive(days=None, current_day=days++) + 1):
            print("Days", n)
    print("Harvest time!")
