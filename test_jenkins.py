def uniq_num(l):
    temp = []
    uniq = []

    for i in l:
        if i not in uniq and i not in temp:
            uniq.append(i)
        else:
            if i in uniq:
                uniq.remove(i)
            temp.append(i)
    return uniq


li = [1, 2, 3, 5, 4, 5, 5, 1]
print(uniq_num(li))
