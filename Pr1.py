mlist = [2, 9, 6, 4, 6, 3, 6]
element_to_remove = 6
count_removed = 0

while element_to_remove in mlist:
    mlist.remove(element_to_remove)
    count_removed += 1

print( mlist)
print(count_removed)
