def ft_count_harvest_recursive(days=None, current_day=1):
    if (days is None):
        days = int(input("Days until harvest: "))
    if (days < current_day):
        print("Harvest time!")
        return
    print("Day", current_day)
    ft_count_harvest_recursive(days, current_day + 1)
