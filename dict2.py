list1 = [1,2,3]
list2 = [1,2,3]
new_list = []
# for i in range(len(list1)):
#     new_list.append(list1[i] + list2[i])

new_list = [list1[i] + list2[i] for i in range(len(list1))]

print(new_list)