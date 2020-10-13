list1 = ["Juniper", "Cisco", "Avaya", 10.5, 11, "Pushkar"]

print(len(list1))
print(list1)
print(list1[2])
list1[2] = "HP"
print(list1[2])
list1.append("HAPPY CODING")
print(list1)

del list1[1]
print(list1)

list2 = [-11, 2, 12]
list3 = ["a", "b", "c"]

print(max(list2))
print(max(list3))
list1.insert(1, "CISCO")
print(list1)

list2.remove(-11)
print(list2)
list3.pop(0)
print(list3)

# To add 2 different list

l1 = [24, 25, 26]
l2 = [27, 28, 29]
# use extend method
l1.extend(l2)
print(l1)
# Sorting in lists
l3 = [2, 99, 81, 56, 43, 78, 90, 12, 9, 65, 100]

# sort l3 in ascending order
l3.sort()
print(l3)

# sort in descending order
l3.reverse()
print(l3)

# using sorted function
sorted(l3)
print(l3)

sorted(l3, reverse= True)
print(l3)