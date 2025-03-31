def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    # return list(s1.intersection(s2))
    return list(s1 & s2)

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 41]

print(inters(l1, l2))
'''
def my_zip(l1, l2):
    if l1
    r = []
    for i in range(len(l1)):
        r.append((l1[i], l2[i]))
             
    return r

'''