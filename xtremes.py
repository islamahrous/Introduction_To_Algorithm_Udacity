def xtrem(lst):
    original_lst = lst.copy()
    if (len(lst) % 2) == 0:
        if lst[0] > lst[1]:
            maxima = lst[0]
            minima = lst[1]
        else:
            minima = lst[0]
            maxima = lst[1]
    else:
        minima = lst[0]
        maxima = lst[0]
        last_element = lst.pop()
    item = 0
    while item < len(lst):
        if lst[item] > lst[item+1]:
            if maxima < lst[item]:
                maxima = lst[item]
            if minima > lst[item+1]:
                minima = lst[item+1]
        else:
            if maxima < lst[item+1]:
                maxima = lst[item+1]
            if minima > lst[item]:
                minima = lst[item]
        item += 2
    if (len(original_lst) % 2) != 0:
        if maxima < last_element:
            maxima = last_element
        if minima > last_element:
            minima = last_element
    return maxima, minima


L = [3, 6, 10, 9, 3]
mxm, mim = xtrem(L)

print(f"The list Max = {mxm}, Min = {mim}")

