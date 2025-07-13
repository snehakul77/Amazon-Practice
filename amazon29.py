#Find duplicates in the list


def duplicated_remove(lst):
    d = {}
    dupli = []
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for k,v in d.items():
        if v > 1:
            dupli.append(k)
    return dupli



duplicates = duplicated_remove([1, 2, 3, 1, 4, 5, 2])
print(duplicates)





