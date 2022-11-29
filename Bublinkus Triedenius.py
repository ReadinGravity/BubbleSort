def BubbleSort(zoz):
    a = len(zoz)
    for i in range(a-1):
        for j in range(a-1):
            if zoz[j] > zoz[j+1]:
                temp = zoz[j]
                zoz[j] = zoz[j+1]
                zoz[j+1] = temp
    return zoz
zoz=[21,6,9,33,3]
print(BubbleSort(zoz))
