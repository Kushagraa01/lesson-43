list=["Apple","Guava","Mango","Kiwi","Cherry"]
print("Lenght of the list is",len(list))
print("First element",list[0])
print("last element",list[-1])

list.append("Papaya")
print("Updated list :",list)

list.remove("Guava")
print("Updated list :",list)

list.sort()
print("Updated list :",list)

list.pop(1)
print("Updated list :",list)

list.reverse()
print("Reverced list is ",list)

print("multiplication on list", list*2)

list=list[:4]
print("Sliced list is ",list)