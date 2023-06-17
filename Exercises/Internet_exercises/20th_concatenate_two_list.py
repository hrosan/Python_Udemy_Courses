'''
Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

list1 = ["Hello","Take"]
list2 = ["Dear","Sir"]
list3 = []

'''
for i in range(len(list1)): # Iterate in each list1's element
    # At this time the loop will iterate in list2 
    for j in range(len(list2)): # Iterate in each list2's element
        list3.append(list1[i]+" "+list2[j]) # Concatenating every element of each list
print(list3)
'''
for i in list1:
    for j in list2:
        list3.append(i+j)
'''
Other way to write the same code
list3 = [x + y for x in list1 for y in list2]
'''
print(list3)